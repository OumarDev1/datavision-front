import os
import sys

root_dir = os.path.abspath(os.path.dirname(__file__))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import streamlit as st
from utils import apply_global_styles, render_header, render_card, render_footer

# 1. Configuration
st.set_page_config(
    page_title="DataVision AI", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

apply_global_styles()

# 2. Header épuré
render_header("🌐 DataVision AI", "Système de monitoring et prédiction environnementale")

# 3. Conteneur principal plus "Light"
st.container(border=True).markdown("""
    <div style='text-align: center; padding: 10px;'>
        <h2 style='margin:0;'>Bienvenue sur votre espace DataVision</h2>
        <p style='color: #64748b;'>Sélectionnez un outil ci-dessous pour démarrer vos analyses.</p>
    </div>
""", unsafe_allow_html=True)

st.write("### 🚀 Accès rapide")

# 4. Grille de navigation
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    render_card("🔮 Prédictions", "Modèle prédictif humidité/CO2/Température.")
    if st.button("Accéder aux Prédictions", use_container_width=True, type="primary"):
        st.switch_page("pages/1_prediction.py")

with col2:
    render_card("📊 Historique", "Visualisez les tendances et logs passés.")
    if st.button("Voir l'Historique", use_container_width=True):
        st.switch_page("pages/2_historique.py")

with col3:
    render_card("⚙️ Configuration", "Paramètres des seuils et notifications.")
    if st.button("Configurer", use_container_width=True):
        st.switch_page("pages/3_configuration.py")

# 5. Footer avec séparation propre
st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
render_footer()