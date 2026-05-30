import streamlit as st
import requests
import random
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="DataVision - IA Dashboard", layout="wide", initial_sidebar_state="expanded")

# --- STYLE CSS ADAPTÉ AU MODE SOMBRE (Correction des cartes blanches) ---
st.markdown("""
    <style>
    .block-container { padding-top: 1.5rem; padding-bottom: 0rem; }
    
    /* Modification des cartes métriques pour le mode sombre */
    div[data-testid="stMetricBlock"] {
        background-color: #1e293b !important; /* Fond bleu nuit/sombre */
        padding: 20px !important; 
        border-radius: 12px !important; 
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1) !important;
        border-left: 5px solid #3b82f6 !important;
    }
    
    /* Assignation des couleurs de bordures gauches spécifiques à chaque carte */
    div[data-testid="stMetricBlock"]:nth-of-type(1) { border-left-color: #3b82f6 !important; } /* Bleu */
    div[data-testid="stMetricBlock"]:nth-of-type(2) { border-left-color: #f59e0b !important; } /* Orange */
    div[data-testid="stMetricBlock"]:nth-of-type(3) { border-left-color: #ef4444 !important; } /* Rouge */
    div[data-testid="stMetricBlock"]:nth-of-type(4) { border-left-color: #10b981 !important; } /* Vert */
    
    /* Forcer la couleur du texte à l'intérieur des cartes pour qu'il soit visible */
    div[data-testid="stMetricLabel"] > div { color: #94a3b8 !important; font-size: 14px !important; }
    div[data-testid="stMetricValue"] > div { color: #ffffff !important; font-size: 28px !important; font-weight: bold !important; }
    </style>
""", unsafe_allow_html=True)

# Barre de navigation supérieure (Style DataVision)
st.markdown("""
    <div style="background-color: #0f172a; padding: 15px; border-radius: 10px; margin-bottom: 25px; display: flex; justify-content: space-between; align-items: center; border: 1px solid #1e293b;">
        <span style="font-weight: bold; font-size: 22px; color: #3b82f6; letter-spacing: 0.5px;">🌐 DataVision AI</span>
        <span style="font-size: 14px; color: #94a3b8;">Tableau de bord principal • Modèle Random Forest connecté</span>
    </div>
""", unsafe_allow_html=True)

# --- ZONE 1 : FORMULAIRE DE SAISIE (Dans la barre latérale gauche) ---
st.sidebar.header("📥 Paramètres des Capteurs (Entrées IA)")

val_humidite = st.sidebar.slider("Humidité (%)", min_value=0.0, max_value=100.0, value=45.5, step=0.1)
val_temperature = st.sidebar.slider("Température (°C)", min_value=-10.0, max_value=50.0, value=24.2, step=0.1)
val_co2 = st.sidebar.number_input("Concentration CO2 (ppm)", min_value=0, max_value=5000, value=450)
val_o2 = st.sidebar.slider("Concentration O2 (%vol)", min_value=0.0, max_value=25.0, value=20.9, step=0.1)

st.sidebar.markdown("---")
btn_analyser = st.sidebar.button("🚀 Lancer l'Analyse IA", use_container_width=True)

# --- VARIABLES DE STRUCTURE INITIALE ---
statut_ia = "En attente"
score_ia = "N/A"
alerte_txt = "Aucune analyse lancée"

if btn_analyser:
    payload = {
        "humidite": val_humidite,
        "temperature": val_temperature,
        "co2": val_co2,
        "o2": val_o2
    }
    
    try:
        response = requests.post("https://datavision-api.onrender.com/predict", json=payload)
        if response.status_code == 200:
            api_result = response.json()
            
            if "status" in api_result and api_result["status"] == "error":
                st.error(f"⚠️ Erreur interne du modèle IA : {api_result['message']}")
            else:
                statut_ia = api_result["statut_environnement"]
                score_ia = str(api_result["score_prediction"])
                alerte_txt = api_result["alerte_message"]
        else:
            st.error("Erreur de communication avec le serveur API.")
    except Exception as e:
        st.error(f"Erreur de connexion au serveur API : {e}")

# --- ZONE 2 : DIAGNOSTICS ET ALERTES ---
st.subheader("🚨 Diagnostics et Alertes Temps Réel")

if statut_ia == "Optimal":
    st.success(f"### ✅ STATUT SYSTÈME : {statut_ia} (Classe {score_ia})  \n**Notification :** {alerte_txt}")
elif statut_ia == "Avertissement":
    st.warning(f"### ⚠️ STATUT SYSTÈME : {statut_ia} (Classe {score_ia})  \n**Alerte :** {alerte_txt}")
elif statut_ia == "Critique":
    st.error(f"### 🚨 STATUT SYSTÈME : {statut_ia} (Classe {score_ia})  \n**Urgence :** {alerte_txt}")
else:
    st.info("### 🕒 Système en attente d'analyse. Modifiez les curseurs et cliquez sur le bouton à gauche.")

st.markdown("<br>", unsafe_allow_html=True)

# --- ZONE 3 : LES CARTES D'INDICATEURS METRICS (Corrigées) ---
st.subheader("📊 Métriques des Capteurs Environnementaux")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="💧 Humidité mesurée", value=f"{val_humidite} %", delta="Stable")
with col2:
    st.metric(label="🌡️ Température", value=f"{val_temperature} °C", delta="En direct")
with col3:
    st.metric(label="⚠️ Message d'Alerte", value=alerte_txt if btn_analyser else "Aucun", delta="Diagnostic")
with col4:
    st.metric(label="🤖 Classe Random Forest", value=score_ia, delta=f"Profil : {statut_ia}")

st.markdown("<br><hr>", unsafe_allow_html=True)

# --- ZONE 4 : GRAPHIQUES CORRIGÉS ---
col_graph1, col_graph2 = st.columns([2, 1])

with col_graph1:
    st.subheader("📈 Activité temporelle des paramètres")
    historique_valeurs = [random.randint(20, 45) for _ in range(15)]
    st.area_chart(historique_valeurs, use_container_width=True)

with col_graph2:
    st.subheader("🍩 Répartition des gaz")
    donnies_gaz = {
        "O2 (%vol)": val_o2,
        "Humidité (%)": val_humidite
    }
    st.bar_chart(donnies_gaz, use_container_width=True)