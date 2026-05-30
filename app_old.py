import streamlit as st
import requests
import random
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="DataVision - IA Dashboard", layout="wide", initial_sidebar_state="expanded")

# --- STYLE CSS AVANCÉ ET DESIGN MODERNE ---
st.markdown("""
    <style>
    /* Configuration générale */
    .block-container { 
        padding-top: 2rem; 
        padding-bottom: 1rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    
    /* Header principal avec dégradé */
    .header-main {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
        padding: 30px;
        border-radius: 15px;
        margin-bottom: 30px;
        border: 2px solid #3b82f6;
        box-shadow: 0 8px 32px rgba(59, 130, 246, 0.15);
        animation: fadeIn 0.5s ease-in;
    }
    
    .header-title {
        font-weight: 900;
        font-size: 32px;
        color: #3b82f6;
        letter-spacing: 1px;
        text-shadow: 0 2px 8px rgba(59, 130, 246, 0.3);
        margin: 0;
        padding-bottom: 10px;
    }
    
    .header-subtitle {
        font-size: 14px;
        color: #64748b;
        margin: 0;
        font-weight: 500;
    }
    
    /* Cartes métriques améliorées */
    div[data-testid="stMetricBlock"] {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%) !important;
        padding: 25px !important; 
        border-radius: 15px !important; 
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3) !important;
        border-left: 6px solid #3b82f6 !important;
        transition: all 0.3s ease !important;
        border-top: 1px solid rgba(59, 130, 246, 0.2) !important;
    }
    
    div[data-testid="stMetricBlock"]:hover {
        box-shadow: 0 12px 24px rgba(59, 130, 246, 0.2) !important;
        transform: translateY(-2px);
    }
    
    /* Couleurs spécifiques des cartes */
    div[data-testid="stMetricBlock"]:nth-of-type(1) { border-left-color: #3b82f6 !important; } /* Bleu */
    div[data-testid="stMetricBlock"]:nth-of-type(2) { border-left-color: #f59e0b !important; } /* Orange */
    div[data-testid="stMetricBlock"]:nth-of-type(3) { border-left-color: #ef4444 !important; } /* Rouge */
    div[data-testid="stMetricBlock"]:nth-of-type(4) { border-left-color: #10b981 !important; } /* Vert */
    
    /* Texte des métriques */
    div[data-testid="stMetricLabel"] > div { 
        color: #94a3b8 !important; 
        font-size: 13px !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px !important;
    }
    
    div[data-testid="stMetricValue"] > div { 
        color: #ffffff !important; 
        font-size: 32px !important; 
        font-weight: 800 !important;
    }
    
    div[data-testid="stMetricDelta"] > div {
        color: #64748b !important;
        font-size: 12px !important;
    }
    
    /* Boutons améliorés */
    .stButton > button {
        border-radius: 10px !important;
        font-weight: 700 !important;
        border: 2px solid #3b82f6 !important;
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%) !important;
        padding: 12px 24px !important;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.6) !important;
        transform: translateY(-2px);
    }
    
    /* Sous-titres */
    h2 {
        color: #e2e8f0 !important;
        font-weight: 700 !important;
        margin-top: 25px !important;
        margin-bottom: 20px !important;
        padding-bottom: 10px !important;
        border-bottom: 2px solid #3b82f6 !important;
    }
    
    /* Messages d'alerte stylisés */
    .stSuccess, .stWarning, .stError, .stInfo {
        border-radius: 12px !important;
        border-left: 5px solid !important;
        padding: 20px !important;
        font-weight: 500 !important;
    }
    
    /* Séparateurs */
    hr { 
        border: 1px solid #334155 !important; 
        margin: 30px 0 !important;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)

# Header principal amélioré
st.markdown("""
    <div class="header-main">
        <div class="header-title">🌐 DataVision AI Dashboard</div>
        <div class="header-subtitle">Analyse intelligente en temps réel • Modèle Random Forest • Monitoring environnemental</div>
    </div>
""", unsafe_allow_html=True)

# --- ZONE 1 : CHOIX DU MODE D'ENTRÉE (Amélioré) ---
st.sidebar.markdown("""
    <div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); padding: 20px; 
                border-radius: 12px; border-left: 4px solid #3b82f6; margin-bottom: 20px;">
        <h2 style="color: #3b82f6; margin: 0; font-size: 18px;">📥 Paramètres Capteurs</h2>
        <p style="color: #94a3b8; margin: 5px 0 0 0; font-size: 12px;">Configuration IA temps réel</p>
    </div>
""", unsafe_allow_html=True)

# Sélecteur de mode amélioré
mode = st.sidebar.radio(
    "📋 Mode de saisie:",
    ("Mode Slider", "Mode Formulaire"),
    horizontal=False,
    label_visibility="visible"
)

st.sidebar.markdown("", unsafe_allow_html=True)

# --- MODE SLIDER (Existant) ---
if mode == "Mode Slider":
    st.sidebar.markdown("### 🎚️ Ajustez les paramètres")
    val_humidite = st.sidebar.slider("💧 Humidité (%)", min_value=0.0, max_value=100.0, value=45.5, step=0.1)
    val_temperature = st.sidebar.slider("🌡️ Température (°C)", min_value=-10.0, max_value=50.0, value=24.2, step=0.1)
    val_co2 = st.sidebar.number_input("💨 Concentration CO2 (ppm)", min_value=0, max_value=5000, value=450)
    val_o2 = st.sidebar.slider("🫁 Concentration O2 (%vol)", min_value=0.0, max_value=25.0, value=20.9, step=0.1)

# --- MODE FORMULAIRE (Nouveau) ---
else:
    st.sidebar.markdown("### 📝 Entrez les paramètres")
    
    col_form1, col_form2 = st.sidebar.columns(2)
    
    with col_form1:
        val_humidite = st.number_input(
            "💧 Humidité (%)",
            min_value=0.0,
            max_value=100.0,
            value=45.5,
            step=0.1
        )
        val_temperature = st.number_input(
            "🌡️ Température (°C)",
            min_value=-10.0,
            max_value=50.0,
            value=24.2,
            step=0.1
        )
    
    with col_form2:
        val_co2 = st.number_input(
            "💨 CO2 (ppm)",
            min_value=0,
            max_value=5000,
            value=450,
            step=1
        )
        val_o2 = st.number_input(
            "🫁 O2 (%vol)",
            min_value=0.0,
            max_value=25.0,
            value=20.9,
            step=0.1
        )

st.sidebar.markdown("---")

btn_analyser = st.sidebar.button("🚀 Lancer l'Analyse IA", use_container_width=True, key="btn_analyze")

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

# Sidebar Footer
st.sidebar.markdown("---")
st.sidebar.markdown("""
    <div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); padding: 15px; 
                border-radius: 10px; border: 1px solid #334155; margin-top: 30px; text-align: center;">
        <p style="color: #64748b; margin: 0; font-size: 11px;">
            <strong>DataVision AI v2.0</strong><br>
            Monitoring Environnemental Intelligent
        </p>
    </div>
""", unsafe_allow_html=True)

# --- ZONE 2 : DIAGNOSTICS ET ALERTES (Amélioré) ---
st.subheader("🚨 Diagnostics et Alertes Temps Réel")

# Conteneur d'alerte stylisé
alert_container = st.container()

with alert_container:
    if statut_ia == "Optimal":
        st.markdown("""
            <div style="background: linear-gradient(135deg, #064e3b 0%, #047857 100%); padding: 25px; border-radius: 12px; 
                        border-left: 5px solid #10b981; box-shadow: 0 8px 16px rgba(16, 185, 129, 0.2);">
                <h3 style="color: #10b981; margin: 0 0 10px 0;">✅ STATUT SYSTÈME : OPTIMAL</h3>
                <p style="color: #d1fae5; margin: 0; font-size: 15px;"><strong>Classe :</strong> {}</p>
                <p style="color: #d1fae5; margin: 5px 0 0 0; font-size: 15px;"><strong>Notification :</strong> {}</p>
            </div>
        """.format(score_ia, alerte_txt), unsafe_allow_html=True)
    elif statut_ia == "Avertissement":
        st.markdown("""
            <div style="background: linear-gradient(135deg, #78350f 0%, #b45309 100%); padding: 25px; border-radius: 12px; 
                        border-left: 5px solid #f59e0b; box-shadow: 0 8px 16px rgba(245, 158, 11, 0.2);">
                <h3 style="color: #f59e0b; margin: 0 0 10px 0;">⚠️ STATUT SYSTÈME : AVERTISSEMENT</h3>
                <p style="color: #fef3c7; margin: 0; font-size: 15px;"><strong>Classe :</strong> {}</p>
                <p style="color: #fef3c7; margin: 5px 0 0 0; font-size: 15px;"><strong>Alerte :</strong> {}</p>
            </div>
        """.format(score_ia, alerte_txt), unsafe_allow_html=True)
    elif statut_ia == "Critique":
        st.markdown("""
            <div style="background: linear-gradient(135deg, #7f1d1d 0%, #dc2626 100%); padding: 25px; border-radius: 12px; 
                        border-left: 5px solid #ef4444; box-shadow: 0 8px 16px rgba(239, 68, 68, 0.2);">
                <h3 style="color: #ef4444; margin: 0 0 10px 0;">🚨 STATUT SYSTÈME : CRITIQUE</h3>
                <p style="color: #fee2e2; margin: 0; font-size: 15px;"><strong>Classe :</strong> {}</p>
                <p style="color: #fee2e2; margin: 5px 0 0 0; font-size: 15px;"><strong>Urgence :</strong> {}</p>
            </div>
        """.format(score_ia, alerte_txt), unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="background: linear-gradient(135deg, #0c4a6e 0%, #0369a1 100%); padding: 25px; border-radius: 12px; 
                        border-left: 5px solid #3b82f6; box-shadow: 0 8px 16px rgba(59, 130, 246, 0.2);">
                <h3 style="color: #3b82f6; margin: 0 0 10px 0;">🕒 Système en attente</h3>
                <p style="color: #bae6fd; margin: 0; font-size: 15px;">Modifiez les paramètres dans la barre latérale et cliquez sur le bouton d'analyse pour commencer</p>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- ZONE 3 : CARTES D'INDICATEURS AMÉLIORÉES ---
st.subheader("📊 Métriques des Capteurs Environnementaux")

col1, col2, col3, col4 = st.columns(4, gap="medium")

with col1:
    st.metric(
        label="💧 Humidité",
        value=f"{val_humidite:.1f}%",
        delta="Stable" if 30 <= val_humidite <= 70 else "⚠️ Anormal"
    )

with col2:
    st.metric(
        label="🌡️ Température",
        value=f"{val_temperature:.1f}°C",
        delta="Confortable" if 20 <= val_temperature <= 26 else "⚠️ À surveiller"
    )

with col3:
    st.metric(
        label="💨 CO2",
        value=f"{val_co2} ppm",
        delta="Normal" if val_co2 <= 1000 else "⚠️ Élevé"
    )

with col4:
    st.metric(
        label="🫁 Oxygène",
        value=f"{val_o2:.1f}%",
        delta="Optimal" if val_o2 >= 19.5 else "⚠️ Bas"
    )

st.markdown("<br><hr>", unsafe_allow_html=True)

# --- ZONE 4 : GRAPHIQUES AMÉLIORÉS ---
st.subheader("📈 Visualisations en Temps Réel")

col_graph1, col_graph2 = st.columns([2, 1], gap="medium")

with col_graph1:
    st.markdown("""
        <div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); 
                    padding: 20px; border-radius: 12px; border: 1px solid #334155; margin-bottom: 15px;">
            <h4 style="color: #3b82f6; margin: 0 0 15px 0; font-size: 16px;">📊 Activité Temporelle des Paramètres</h4>
    """, unsafe_allow_html=True)
    
    historique_valeurs = [random.randint(20, 45) for _ in range(15)]
    st.area_chart(historique_valeurs, use_container_width=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

with col_graph2:
    st.markdown("""
        <div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); 
                    padding: 20px; border-radius: 12px; border: 1px solid #334155; margin-bottom: 15px;">
            <h4 style="color: #3b82f6; margin: 0 0 15px 0; font-size: 16px;">🍩 Répartition Atmosphérique</h4>
    """, unsafe_allow_html=True)
    
    donnies_gaz = {
        "O2 (%vol)": val_o2,
        "Humidité (%)": val_humidite
    }
    st.bar_chart(donnies_gaz, use_container_width=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Section Footer avec statistiques
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
    <div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); padding: 20px; border-radius: 12px; 
                border-left: 4px solid #3b82f6; margin-top: 20px; text-align: center;">
        <p style="color: #64748b; margin: 0; font-size: 12px;">
            🔄 Dernier update : en temps réel | 📡 Connexion API : Active | 🤖 Modèle : Random Forest v1.0
        </p>
    </div>
""", unsafe_allow_html=True)