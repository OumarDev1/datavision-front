import importlib.util
import os
import sys

import streamlit as st
from utils import apply_global_styles, render_header, render_card, render_footer

# Configuration de la page
st.set_page_config(
    page_title="DataVision - IA Platform", 
    layout="wide", 
    initial_sidebar_state="expanded",
    menu_items={
        "About": "DataVision AI Platform v2.0 - Prédiction environnementale intelligente"
    }
)

# Appliquer les styles globaux
apply_global_styles()

# Sidebar - Navigation et informations
st.sidebar.markdown("""
    <div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); padding: 20px; 
                border-radius: 12px; border-left: 4px solid #3b82f6; margin-bottom: 20px;">
        <h2 style="color: #3b82f6; margin: 0; font-size: 18px;">🌐 DataVision AI</h2>
        <p style="color: #94a3b8; margin: 5px 0 0 0; font-size: 12px;">Plateforme de Prédiction</p>
    </div>
""", unsafe_allow_html=True)

if "page_choice" not in st.session_state:
    st.session_state.page_choice = "🏠 Dashboard"

page_choice = st.sidebar.selectbox(
    "📍 Aller à :",
    [
        "🏠 Dashboard",
        "🔮 Prédictions",
        "📊 Historique",
        "⚙️ Configuration",
        "📚 Documentation"
    ],
    key="page_choice"
)

page_mapping = {
    "🔮 Prédictions": os.path.join("pages", "1_prediction.py"),
    "📊 Historique": os.path.join("pages", "2_historique.py"),
    "⚙️ Configuration": os.path.join("pages", "3_configuration.py"),
    "📚 Documentation": os.path.join("pages", "4_documentation.py")
}


def navigate_to(page_name: str):
    if "page_choice" not in st.session_state:
        st.session_state.page_choice = "🏠 Dashboard"
    st.session_state.page_choice = page_name
    st.experimental_rerun()


def run_page(path):
    module_name = f"page_{os.path.splitext(os.path.basename(path))[0]}"
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

if page_choice != "🏠 Dashboard":
    run_page(page_mapping[page_choice])
    st.stop()

# --- Page d'accueil simple ---
render_header("🌐 DataVision AI", "Un point d’entrée clair pour vos analyses environnementales")

st.markdown(
    """
    <div style='background: rgba(59, 130, 246, 0.1); padding: 24px; border-radius: 18px;'>
        <h2 style='color: #e2e8f0; margin: 0 0 10px 0;'>Bienvenue sur DataVision</h2>
        <p style='color: #cbd5e1; margin: 0; font-size: 15px; line-height: 1.7;'>
            Une interface claire et accessible pour prédire l'état de l’environnement, suivre l'historique de vos analyses et ajuster vos paramètres.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("### Accès rapide")

col_pred, col_hist, col_conf = st.columns(3, gap="large")

with col_pred:
    render_card(
        "🔮 Prédictions",
        "Saisissez vos paramètres et obtenez une prédiction instantanée pour humidité, température, CO2 et O2."
    )
    st.button("Ouvrir", key="go_predict", on_click=navigate_to, args=("🔮 Prédictions",))

with col_hist:
    render_card(
        "📊 Historique",
        "Visualisez vos analyses précédentes et suivez l’évolution de votre environnement."
    )
    st.button("Ouvrir", key="go_history", on_click=navigate_to, args=("📊 Historique",))

with col_conf:
    render_card(
        "⚙️ Configuration",
        "Ajustez les seuils d’alerte, notifications et préférences de la plateforme."
    )
    st.button("Ouvrir", key="go_settings", on_click=navigate_to, args=("⚙️ Configuration",))

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Pourquoi utiliser DataVision ?")

st.markdown(
    """
    <div class='card'>
        <ul style='color: #cbd5e1; margin: 0 0 0 18px; line-height: 1.8;'>
            <li>Interface simple et lisible, sans surcharge d’information.</li>
            <li>Navigation claire entre l’accueil, les prédictions, l’historique et les paramètres.</li>
            <li>Alertes visuelles et sonores pour réagir rapidement aux situations critiques.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

st.info(
    "Pour démarrer, cliquez sur l’une des cartes ci-dessus ou utilisez le menu latéral."
)

render_footer()
