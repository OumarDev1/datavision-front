"""
Page Historique : affiche les prédictions réellement faites par l'utilisateur,
lues depuis la base SQLite (database.get_predictions), avec un code couleur
sur le statut et un téléchargement CSV (CU06).
"""
import streamlit as st
import pandas as pd

from database import get_predictions
from utils import apply_global_styles, render_header

st.set_page_config(page_title="Historique", layout="wide")
apply_global_styles()
render_header("📋 Détail des Prédictions", "Historique de vos prédictions")

df = get_predictions()

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
    })
    affichage["ID"] = affichage["ID"].apply(lambda x: f"#{x:07d}")
    affichage["Précision"] = affichage["Précision"].apply(
        lambda x: f"{x * 100:.0f}%" if pd.notna(x) else "-"
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
