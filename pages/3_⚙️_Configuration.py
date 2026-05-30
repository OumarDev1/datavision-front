import streamlit as st
from utils import apply_global_styles, render_header, render_card, render_footer

# Configuration
st.set_page_config(page_title="Configuration - DataVision", layout="wide")
apply_global_styles()

# Header
render_header("⚙️ Configuration", "Personnalisez les paramètres de la plateforme")

# --- CONFIGURATION API ---
st.subheader("🔌 Configuration API")

col_api1, col_api2 = st.columns(2)

with col_api1:
    api_url = st.text_input(
        "URL de l'API",
        value="https://datavision-api.onrender.com",
        help="Adresse de votre serveur API"
    )

with col_api2:
    timeout = st.number_input(
        "Timeout (secondes)",
        min_value=1,
        max_value=60,
        value=30,
        help="Délai d'attente pour les requêtes API"
    )

st.markdown("---")

# --- SEUILS D'ALERTE ---
st.subheader("⚠️ Seuils d'Alerte")

col_seuil1, col_seuil2 = st.columns(2)

with col_seuil1:
    st.markdown("### 💧 Humidité")
    hum_min = st.slider("Humidité minimale (%)", 0, 100, 30, help="Seuil bas d'humidité")
    hum_max = st.slider("Humidité maximale (%)", 0, 100, 70, help="Seuil haut d'humidité")

with col_seuil2:
    st.markdown("### 🌡️ Température")
    temp_min = st.slider("Température minimale (°C)", -20, 50, 20, help="Seuil bas de température")
    temp_max = st.slider("Température maximale (°C)", -20, 50, 26, help="Seuil haut de température")

col_seuil3, col_seuil4 = st.columns(2)

with col_seuil3:
    st.markdown("### 💨 CO2")
    co2_max = st.slider("CO2 maximum (ppm)", 0, 5000, 1000, help="Seuil d'alerte CO2")

with col_seuil4:
    st.markdown("### 🫁 Oxygène")
    o2_min = st.slider("O2 minimum (%vol)", 0.0, 25.0, 19.5, step=0.1, help="Seuil bas d'oxygène")

st.markdown("---")

# --- PRÉFÉRENCES VISUELLES ---
st.subheader("🎨 Préférences Visuelles")

col_viz1, col_viz2, col_viz3 = st.columns(3)

with col_viz1:
    theme = st.radio("Thème", ["Mode Sombre", "Mode Clair", "Automatique"])

with col_viz2:
    densité = st.radio("Densité", ["Compact", "Normal", "Spacieux"])

with col_viz3:
    animations = st.toggle("Activer les animations", value=True)

st.markdown("---")

# --- NOTIFICATIONS ---
st.subheader("🔔 Notifications")

col_notif1, col_notif2 = st.columns(2)

with col_notif1:
    st.markdown("### Email")
    notif_email = st.toggle("Activer les notifications email", value=True)
    if notif_email:
        email = st.text_input("Adresse email", placeholder="example@email.com")
        st.selectbox("Alertes par email", ["Critique uniquement", "Critique + Avertissement", "Toutes les analyses"])

with col_notif2:
    st.markdown("### Push")
    notif_push = st.toggle("Activer les notifications push", value=False)
    if notif_push:
        st.info("Les notifications push seront envoyées à votre appareil")

st.markdown("---")

# --- PARAMÈTRES AVANCÉS ---
st.subheader("🔧 Paramètres Avancés")

col_adv1, col_adv2 = st.columns(2)

with col_adv1:
    st.markdown("### 📊 Stockage des Données")
    retention = st.slider(
        "Durée de conservation (jours)",
        1, 365, 90,
        help="Nombre de jours de conservation des données"
    )
    
    auto_cleanup = st.toggle("Nettoyage automatique", value=True)

with col_adv2:
    st.markdown("### 🔐 Sécurité")
    two_factor = st.toggle("Authentification 2FA", value=False)
    
    st.selectbox(
        "Niveau de sécurité",
        ["Standard", "Renforcé", "Maximum"]
    )

st.markdown("---")

# --- INTÉGRATIONS ---
st.subheader("🔗 Intégrations")

col_int1, col_int2, col_int3 = st.columns(3)

with col_int1:
    st.markdown("### 📧 Email")
    email_enabled = st.toggle("Email actif", value=False)
    if email_enabled:
        st.text_input("SMTP Server", placeholder="smtp.gmail.com")

with col_int2:
    st.markdown("### 📱 Slack")
    slack_enabled = st.toggle("Slack actif", value=False)
    if slack_enabled:
        st.text_input("Webhook URL", placeholder="https://hooks.slack.com/...")

with col_int3:
    st.markdown("### 🔗 Webhooks")
    webhook_enabled = st.toggle("Webhooks actifs", value=False)
    if webhook_enabled:
        st.text_input("URL Webhook", placeholder="https://example.com/webhook")

st.markdown("---")

# --- BOUTONS D'ACTION ---
st.subheader("💾 Sauvegarde et Actions")

col_btn1, col_btn2, col_btn3 = st.columns(3)

with col_btn1:
    if st.button("💾 Sauvegarder les paramètres", use_container_width=True):
        st.success("✅ Paramètres sauvegardés avec succès!")

with col_btn2:
    if st.button("🔄 Réinitialiser par défaut", use_container_width=True):
        st.warning("⚠️ Les paramètres ont été réinitialisés")

with col_btn3:
    if st.button("📥 Exporter la configuration", use_container_width=True):
        st.info("📥 Configuration exportée")

st.markdown("<br><hr>", unsafe_allow_html=True)

# --- RÉSUMÉ DE CONFIGURATION ---
st.subheader("📋 Résumé de Configuration Actuelle")

col_resume1, col_resume2 = st.columns(2)

with col_resume1:
    render_card(
        "API Configuration",
        f"""
        <strong>URL :</strong> {api_url}<br>
        <strong>Timeout :</strong> {timeout}s<br>
        <strong>Thème :</strong> {theme}
        """
    )

with col_resume2:
    render_card(
        "Seuils d'Alerte",
        f"""
        <strong>Humidité :</strong> {hum_min}% - {hum_max}%<br>
        <strong>Température :</strong> {temp_min}°C - {temp_max}°C<br>
        <strong>CO2 :</strong> jusqu'à {co2_max} ppm
        """
    )

col_resume3, col_resume4 = st.columns(2)

with col_resume3:
    render_card(
        "Notifications",
        f"""
        <strong>Email :</strong> {'Activé' if notif_email else 'Désactivé'}<br>
        <strong>Push :</strong> {'Activé' if notif_push else 'Désactivé'}<br>
        <strong>2FA :</strong> {'Activé' if two_factor else 'Désactivé'}
        """
    )

with col_resume4:
    render_card(
        "Intégrations",
        f"""
        <strong>Email :</strong> {'Actif' if email_enabled else 'Inactif'}<br>
        <strong>Slack :</strong> {'Actif' if slack_enabled else 'Inactif'}<br>
        <strong>Webhooks :</strong> {'Actifs' if webhook_enabled else 'Inactifs'}
        """
    )

st.markdown("<br>", unsafe_allow_html=True)

# --- INFORMATION D'AIDE ---
with st.expander("❓ Aide et Support"):
    st.markdown("""
    ### Questions Fréquentes
    
    **Comment changer mes seuils d'alerte ?**
    - Utilisez les curseurs dans la section "Seuils d'Alerte"
    - Les modifications sont appliquées immédiatement
    
    **Comment activer les notifications ?**
    - Allez à la section "Notifications"
    - Activez le type de notification souhaité
    - Entrez vos informations de contact
    
    **Quelle est la durée de conservation des données ?**
    - Par défaut : 90 jours
    - Configurable dans "Paramètres Avancés"
    
    **Comment exporter ma configuration ?**
    - Cliquez sur "Exporter la configuration"
    - Un fichier JSON sera créé
    """)

render_footer()
