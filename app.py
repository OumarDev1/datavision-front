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

page_choice = st.sidebar.selectbox(
    "📍 Aller à :",
    [
        "🏠 Dashboard",
        "🔮 Prédictions",
        "📊 Historique",
        "⚙️ Configuration",
        "📚 Documentation"
    ],
    index=0
)

page_mapping = {
    "🔮 Prédictions": os.path.join("pages", "1_prediction.py"),
    "📊 Historique": os.path.join("pages", "2_historique.py"),
    "⚙️ Configuration": os.path.join("pages", "3_configuration.py"),
    "📚 Documentation": os.path.join("pages", "4_documentation.py")
}


def run_page(path):
    module_name = f"page_{os.path.splitext(os.path.basename(path))[0]}"
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

if page_choice != "🏠 Dashboard":
    run_page(page_mapping[page_choice])
    st.stop()

# Afficher le header principal
render_header("🌐 DataVision AI Platform", "Tableau de bord principal • Analyse environnementale en temps réel")

# --- CONTENU PRINCIPAL ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="📊 Prédictions Total",
        value="1,234",
        delta="↑ 52 cette semaine"
    )

with col2:
    st.metric(
        label="✅ Taux de Précision",
        value="94.3%",
        delta="↑ +2.1%"
    )

with col3:
    st.metric(
        label="⚡ Modèles Actifs",
        value="5",
        delta="Tous opérationnels"
    )

st.markdown("<br>", unsafe_allow_html=True)

# --- SECTION FEATURES ---
st.subheader("🚀 Fonctionnalités Principales")

col_f1, col_f2, col_f3 = st.columns(3)

with col_f1:
    render_card(
        "🔮 Prédictions",
        "Analysez les paramètres environnementaux avec deux modes de saisie : Slider et Formulaire. Obtenez des prédictions en temps réel."
    )

with col_f2:
    render_card(
        "📊 Historique",
        "Consultez l'historique complet de vos analyses. Suivez les tendances et les patterns au fil du temps."
    )

with col_f3:
    render_card(
        "⚙️ Configuration",
        "Personnalisez les paramètres de la plateforme, gérez les seuils d'alerte et configurez vos préférences."
    )

st.markdown("<br>", unsafe_allow_html=True)

# --- SECTION STATISTIQUES ---
st.subheader("📈 Statistiques Globales")

col_stats1, col_stats2, col_stats3 = st.columns(3)

with col_stats1:
    st.markdown("""
        <div class="card">
            <h4 style="color: #3b82f6; margin: 0;">📌 Paramètres Analysés</h4>
            <p style="color: #64748b; font-size: 24px; font-weight: bold; margin: 15px 0;">4</p>
            <p style="color: #94a3b8; margin: 0; font-size: 12px;">Humidité • Température • CO2 • O2</p>
        </div>
    """, unsafe_allow_html=True)

with col_stats2:
    st.markdown("""
        <div class="card">
            <h4 style="color: #f59e0b; margin: 0;">🤖 Modèle IA</h4>
            <p style="color: #64748b; font-size: 24px; font-weight: bold; margin: 15px 0;">Random Forest</p>
            <p style="color: #94a3b8; margin: 0; font-size: 12px;">Algorithme de classification avancé</p>
        </div>
    """, unsafe_allow_html=True)

with col_stats3:
    st.markdown("""
        <div class="card">
            <h4 style="color: #10b981; margin: 0;">🔌 API Status</h4>
            <p style="color: #64748b; font-size: 24px; font-weight: bold; margin: 15px 0;">Active</p>
            <p style="color: #94a3b8; margin: 0; font-size: 12px;">Connecté au serveur Render</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- GUIDE RAPIDE ---
st.subheader("📖 Guide de Démarrage Rapide")

with st.expander("ℹ️ Comment utiliser la plateforme ?"):
    st.markdown("""
    ### Étapes simples pour commencer :
    
    1. **🔮 Prédictions** : Accédez à la page de prédiction via le menu latéral
    2. **⚙️ Configurez** : Choisissez entre le mode Slider ou Formulaire
    3. **📊 Analysez** : Entrez vos paramètres et cliquez sur "Lancer l'Analyse"
    4. **📈 Consultez** : Explorez votre historique et les tendances
    
    ### Mode Slider
    - Interface intuitive avec des curseurs
    - Idéal pour les ajustements rapides
    - Visualisation en temps réel des changements
    
    ### Mode Formulaire
    - Saisie précise des valeurs
    - Meilleur pour les analyses détaillées
    - Entrée par champs numériques
    """)

with st.expander("⚠️ Comprendre les statuts"):
    st.markdown("""
    | Statut | Signification | Action |
    |--------|---------------|--------|
    | ✅ **Optimal** | Conditions parfaites | Aucune action requise |
    | ⚠️ **Avertissement** | Conditions à surveiller | Surveillance recommandée |
    | 🚨 **Critique** | Conditions dangereuses | Action immédiate requise |
    """)

st.markdown("<br>", unsafe_allow_html=True)

# --- RECENT INSIGHTS ---
st.subheader("💡 Insights Récents")

col_insight1, col_insight2 = st.columns(2)

with col_insight1:
    st.info("""
    **📊 Tendance Humidité** : Les niveaux d'humidité sont restés stables 
    cette semaine avec une moyenne de 45.3%. Conditions optimales maintenues.
    """)

with col_insight2:
    st.warning("""
    **🌡️ Alerte Température** : La température a augmenté de 2.5°C cette semaine. 
    Recommandation : augmenter la ventilation.
    """)

st.markdown("<br>", unsafe_allow_html=True)

# Footer
render_footer()
