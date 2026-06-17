"""
Page Historique : affiche les prédictions réellement faites par l'utilisateur,
lues depuis la base SQLite (database.get_predictions), avec un code couleur
sur le statut et un téléchargement CSV (CU06).
"""
import os
import sys

import streamlit as st
import pandas as pd

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from database import get_predictions, vider_historique
try:
    from utils import apply_global_styles, render_header
except ImportError:
    import importlib.util
    utils_path = os.path.join(root_dir, "utils.py")
    spec = importlib.util.spec_from_file_location("utils", utils_path)
    utils = importlib.util.module_from_spec(spec)
    sys.modules["utils"] = utils
    spec.loader.exec_module(utils)
    apply_global_styles = utils.apply_global_styles
    render_header = utils.render_header

st.set_page_config(page_title="Historique", layout="wide")
apply_global_styles()
render_header("📋 Détail des Prédictions", "Historique de vos prédictions")
# Récupérer les prédictions et préparer l'export CSV
df = get_predictions()
csv_export = df.to_csv(index=False).encode("utf-8") if not df.empty else b""

# Confirmation suppression
if "confirm_delete" not in st.session_state:
    st.session_state["confirm_delete"] = False

col_main, col_action = st.columns([7, 2])
with col_action:
    if st.download_button(
        "📥 Exporter",
        data=csv_export,
        file_name="historique_predictions.csv",
        mime="text/csv",
        key="export_csv"
    ):
        pass

    if st.button("🗑️ Effacer l'historique"):
        st.session_state["confirm_delete"] = True

if st.session_state.get("confirm_delete"):
    st.warning("Vous êtes sur le point de supprimer définitivement tout l'historique.")
    col_yes, col_no = st.columns([1, 1])
    with col_yes:
        if st.button("Confirmer la suppression"):
            vider_historique()
            st.session_state["confirm_delete"] = False
            st.success("Historique effacé.")
            st.experimental_rerun()
    with col_no:
        if st.button("Annuler"):
            st.session_state["confirm_delete"] = False

# df already chargé plus haut

if df.empty:
    st.info(
        "Aucune prédiction enregistrée pour le moment. "
        "Rendez-vous dans le menu Prédiction pour en effectuer une."
    )
else:
    # --- Préparer l'affichage ---
    affichage = df.rename(columns={
        "id": "ID",
        "date_heure": "Date/Heure",
        "humidite": "Humidité",
        "temperature": "Température",
        "co2": "CO2",
        "o2": "O2",
        "statut": "Statut",
        "precision": "Précision",
        "score": "Score (%)",
        "message": "Commentaire",
    })
    affichage["ID"] = affichage["ID"].apply(lambda x: f"#{x:07d}")
    if "Précision" in affichage.columns:
        affichage["Précision"] = affichage["Précision"].apply(
            lambda x: f"{x * 100:.0f}%" if pd.notna(x) else "-"
        )
    if "Score (%)" in affichage.columns:
        affichage["Score (%)"] = affichage["Score (%)"].apply(
            lambda x: f"{x:.0f}%" if pd.notna(x) else "-"
        )

    # --- Couleur du statut ---
    def colorer_statut(val):
        v = str(val).lower()
        if v in ("optimal", "faible"):
            return "background-color:#dcfce7; color:#15803d;"
        if v in ("avertissement", "modéré", "modere"):
            return "background-color:#fef9c3; color:#a16207;"
        if v in ("critique", "élevé", "eleve"):
            return "background-color:#fee2e2; color:#b91c1c;"
        return ""

    # .map nécessite pandas >= 2.1 ; pour une version plus ancienne,
    # remplace .map par .applymap.
    styled = affichage.style.map(colorer_statut, subset=["Statut"])
    st.dataframe(styled, use_container_width=True, hide_index=True)

    # --- Statistiques rapides ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Total prédictions", len(df))
    col2.metric("Cas critiques",
                int((df["statut"].str.lower().isin(["critique", "élevé", "eleve"])).sum()))
    col3.metric("Dernière prédiction", df["date_heure"].iloc[0])

    # --- Téléchargement CSV (CU06) ---
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "📥 Télécharger CSV",
        data=csv,
        file_name="historique_predictions.csv",
        mime="text/csv",
    )
