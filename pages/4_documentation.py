import os
import sys

import streamlit as st

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

try:
    from utils import apply_global_styles, render_header, render_card, render_footer
except ImportError:
    import importlib.util
    utils_path = os.path.join(root_dir, "utils.py")
    spec = importlib.util.spec_from_file_location("utils", utils_path)
    utils = importlib.util.module_from_spec(spec)
    sys.modules["utils"] = utils
    spec.loader.exec_module(utils)
    apply_global_styles = utils.apply_global_styles
    render_header = utils.render_header
    render_card = utils.render_card
    render_footer = utils.render_footer

# Configuration
if __name__ == "__main__":
    st.set_page_config(page_title="Documentation - DataVision", layout="wide")
apply_global_styles()

# Header
render_header("📚 Documentation", "Guide complet de la plateforme DataVision AI")

# --- TABLE OF CONTENTS ---
st.subheader("📑 Table des Matières")

toc_cols = st.columns(3)

with toc_cols[0]:
    st.markdown("""
    ### 🔰 Démarrage Rapide
    - [Guide d'installation](#installation)
    - [Configuration initiale](#configuration)
    - [Première prédiction](#premiere-prediction)
    """)

with toc_cols[1]:
    st.markdown("""
    ### 🔮 Utilisation
    - [Page Prédictions](#predictions)
    - [Page Historique](#historique)
    - [Configuration](#configuration)
    """)

with toc_cols[2]:
    st.markdown("""
    ### 🔧 Technique
    - [Architecture API](#api)
    - [Paramètres](#parametres)
    - [FAQ](#faq)
    """)

st.markdown("---")

# --- GUIDE D'INSTALLATION ---
st.subheader("🔰 Démarrage Rapide", anchor="installation")

with st.expander("📥 Installation", expanded=True):
    st.markdown("""
    ### Prérequis
    - Python 3.8+
    - pip ou conda
    
    ### Étapes d'installation
    
    1. **Clonez le repository**
    ```bash
    git clone https://github.com/votre-repo/datavision.git
    cd datavision
    ```
    
    2. **Créez un environnement virtuel**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    # ou
    venv\\Scripts\\activate  # Windows
    ```
    
    3. **Installez les dépendances**
    ```bash
    pip install -r requirements.txt
    ```
    
    4. **Lancez l'application**
    ```bash
    streamlit run app.py
    ```
    """)

with st.expander("⚙️ Configuration Initiale", expanded=False):
    st.markdown("""
    ### Configuration de l'API
    
    1. Allez à la page **Configuration**
    2. Entrez l'URL de votre serveur API
    3. Configurez les seuils d'alerte selon vos besoins
    4. Activez les notifications si souhaité
    
    ### Paramètres Recommandés
    
    | Paramètre | Valeur par défaut | Recommandation |
    |-----------|------------------|-----------------|
    | Humidité min | 30% | 30-35% |
    | Humidité max | 70% | 65-70% |
    | Température min | 20°C | 18-20°C |
    | Température max | 26°C | 24-26°C |
    | CO2 max | 1000 ppm | 800-1000 ppm |
    | O2 min | 19.5% | 19.5% |
    """)

st.markdown("---")

# --- PAGE PRÉDICTIONS ---
st.subheader("🔮 Page Prédictions", anchor="predictions")

with st.expander("Mode Slider", expanded=True):
    st.markdown("""
    ### Utilisation
    
    Le **Mode Slider** offre une interface intuitive avec des curseurs pour ajuster les paramètres.
    
    **Avantages:**
    - Interface rapide et fluide
    - Visualisation en temps réel
    - Idéal pour les explorations
    
    **Paramètres:**
    - 💧 **Humidité** : 0% - 100%
    - 🌡️ **Température** : -10°C - 50°C
    - 💨 **CO2** : 0 - 5000 ppm
    - 🫁 **O2** : 0% - 25%
    
    ### Étapes
    1. Accédez à la page "🔮 Prédictions"
    2. Sélectionnez "Mode Slider"
    3. Ajustez les curseurs selon vos paramètres
    4. Cliquez sur "🚀 Lancer l'Analyse"
    """)

with st.expander("Mode Formulaire", expanded=False):
    st.markdown("""
    ### Utilisation
    
    Le **Mode Formulaire** permet une saisie précise des valeurs par champs numériques.
    
    **Avantages:**
    - Saisie précise au centième
    - Idéal pour l'import de données
    - Meilleure pour les analyses détaillées
    
    **Étapes**
    1. Accédez à la page "🔮 Prédictions"
    2. Sélectionnez "Mode Formulaire"
    3. Entrez les valeurs dans les champs
    4. Cliquez sur "🚀 Lancer l'Analyse"
    """)

with st.expander("Comprendre les Résultats", expanded=False):
    st.markdown("""
    ### Statuts de Prédiction
    
    **✅ OPTIMAL**
    - Tous les paramètres sont dans les normes
    - Aucune action requise
    - Score prédictif élevé
    
    **⚠️ AVERTISSEMENT**
    - Un ou plusieurs paramètres sont hors normes
    - Surveillance recommandée
    - Action à court terme possible
    
    **🚨 CRITIQUE**
    - Situation dangereuse ou anormale
    - Action immédiate requise
    - Intervention recommandée
    
    ### Métriques Affichées
    - Valeurs actuelles de chaque paramètre
    - Comparaison avec les normes
    - Message d'alerte détaillé
    - Graphiques de tendance
    - Recommandations spécifiques
    """)

st.markdown("---")

# --- PAGE HISTORIQUE ---
st.subheader("📊 Page Historique", anchor="historique")

with st.expander("Filtrer et Analyser", expanded=True):
    st.markdown("""
    ### Fonctionnalités
    
    1. **Filtrage par date**
       - Définissez une plage de dates
       - Consultez les données spécifiques
    
    2. **Filtrage par statut**
       - Tous les statuts
       - Optimal uniquement
       - Avertissements
       - Critiques
    
    3. **Statistiques**
       - Nombre total d'analyses
       - Pourcentage par statut
       - Moyennes par paramètre
    
    4. **Graphiques**
       - Distribution des statuts
       - Tendances temporelles
       - Comparaisons entre paramètres
    """)

with st.expander("Télécharger les Données", expanded=False):
    st.markdown("""
    ### Export des Données
    
    Vous pouvez exporter votre historique en format CSV pour :
    - Analyse dans Excel/Sheets
    - Import dans d'autres outils
    - Sauvegarde locale
    - Partage avec d'autres utilisateurs
    
    **Comment télécharger:**
    1. Appliquez vos filtres
    2. Cliquez sur "📥 Télécharger CSV"
    3. Le fichier est sauvegardé automatiquement
    """)

st.markdown("---")

# --- ARCHITECTURE API ---
st.subheader("🔧 Architecture API", anchor="api")

with st.expander("Endpoint de Prédiction", expanded=True):
    st.markdown("""
    ### POST /predict
    
    **URL:** `https://datavision-api.onrender.com/predict`
    
    **Paramètres (JSON):**
    ```json
    {
        "humidite": 45.5,
        "temperature": 24.2,
        "co2": 450,
        "o2": 20.9
    }
    ```
    
    **Réponse réussie:**
    ```json
    {
        "statut_environnement": "Optimal",
        "score_prediction": 1,
        "alerte_message": "Conditions optimales maintenues..."
    }
    ```
    
    **Erreur:**
    ```json
    {
        "status": "error",
        "message": "Description de l'erreur"
    }
    ```
    
    **Codes de statut:**
    - `200` : Succès
    - `400` : Paramètres invalides
    - `500` : Erreur serveur
    """)

with st.expander("Format des Données", expanded=False):
    st.markdown("""
    ### Paramètres d'Entrée
    
    | Paramètre | Type | Plage | Unité |
    |-----------|------|-------|-------|
    | humidite | float | 0-100 | % |
    | temperature | float | -10-50 | °C |
    | co2 | int | 0-5000 | ppm |
    | o2 | float | 0-25 | %vol |
    
    ### Paramètres de Sortie
    
    | Paramètre | Type | Valeurs |
    |-----------|------|--------|
    | statut_environnement | string | "Optimal" / "Avertissement" / "Critique" |
    | score_prediction | int | 0 / 1 / 2 |
    | alerte_message | string | Message détaillé |
    """)

st.markdown("---")

# --- PARAMÈTRES DÉTAILLÉS ---
st.subheader("📊 Paramètres Environnementaux", anchor="parametres")

param_cols = st.columns(2)

with param_cols[0]:
    with st.expander("💧 Humidité"):
        st.markdown("""
        **Plage normale:** 30% - 70%
        
        **Impacts:**
        - **Trop basse** : Sécheresse, dégradation
        - **Normale** : Conditions optimales
        - **Trop élevée** : Moisissures, condensation
        
        **Recommandations:**
        - Surveillance continue
        - Ventilation si trop élevée
        - Humidification si trop basse
        """)
    
    with st.expander("🌡️ Température"):
        st.markdown("""
        **Plage optimale:** 20°C - 26°C
        
        **Impacts:**
        - **Trop basse** : Inconfort, ralentissement
        - **Normale** : Conditions optimales
        - **Trop élevée** : Inconfort, consommation énergétique
        
        **Recommandations:**
        - Ajustement du chauffage/climatisation
        - Isolation thermique
        - Ventilation naturelle si possible
        """)

with param_cols[1]:
    with st.expander("💨 Dioxyde de Carbone"):
        st.markdown("""
        **Seuil d'alerte:** 1000 ppm
        
        **Impacts:**
        - **Normal** : < 800 ppm - Optimal
        - **Élevé** : 800-1200 ppm - Attention
        - **Critique** : > 1200 ppm - Action requise
        
        **Recommandations:**
        - Augmenter la ventilation
        - Améliorer la circulation d'air
        - Installations de filtration
        """)
    
    with st.expander("🫁 Oxygène"):
        st.markdown("""
        **Plage normale:** 19.5% - 21%
        
        **Impacts:**
        - **Bas** : < 19.5% - Dangereux
        - **Normal** : 19.5-21% - Optimal
        - **Élevé** : > 21% - Rare
        
        **Recommandations:**
        - Ventilation immédiate si bas
        - Prévention de la suffocation
        - Contrôle des gaz
        """)

st.markdown("---")

# --- FAQ ---
st.subheader("❓ Questions Fréquemment Posées", anchor="faq")

faqs = {
    "Pourquoi mes prédictions ne sont pas précises ?": 
        "Vérifiez que vos capteurs sont calibrés correctement et que les valeurs entrées sont exactes.",
    
    "Comment changer mes seuils d'alerte ?": 
        "Allez à la page Configuration et ajustez les curseurs dans la section 'Seuils d'Alerte'.",
    
    "Combien de temps les données sont conservées ?": 
        "Par défaut 90 jours, configurable dans Paramètres Avancés.",
    
    "Puis-je exporter mes données ?": 
        "Oui, via la page Historique avec le bouton 'Télécharger CSV'.",
    
    "L'API est-elle disponible 24/7 ?": 
        "Oui, notre API fonctionne 24/7 avec un uptime de 99.9%.",
    
    "Comment activer les notifications ?": 
        "Allez à Configuration > Notifications et activez l'option souhaitée.",
}

for question, answer in faqs.items():
    with st.expander(question):
        st.markdown(answer)

st.markdown("---")

# --- SUPPORT ---
st.subheader("📞 Support et Contacte")

col_sup1, col_sup2, col_sup3 = st.columns(3)

with col_sup1:
    render_card(
        "📧 Email",
        "support@datavision.com"
    )

with col_sup2:
    render_card(
        "💬 Chat",
        "Disponible sur la plateforme"
    )

with col_sup3:
    render_card(
        "📚 Documentation",
        "docs.datavision.com"
    )

render_footer()
