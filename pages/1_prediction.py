import streamlit as st
import requests
import random
import pandas as pd
from datetime import datetime, timedelta
from utils import apply_global_styles, render_header, render_alert_box, render_warning_alert, render_critical_alert, render_footer, save_prediction
# Configuration
if __name__ == "__main__":
    st.set_page_config(page_title="Prédictions - DataVision", layout="wide")
apply_global_styles()

# Header
render_header("🔮 Centre de Prédictions", "Analysez vos données environnementales en temps réel")

# Sidebar - Contrôles
st.sidebar.markdown("""
    <div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); padding: 20px; 
                border-radius: 12px; border-left: 4px solid #3b82f6; margin-bottom: 20px;">
        <h2 style="color: #3b82f6; margin: 0; font-size: 18px;">📥 Paramètres</h2>
        <p style="color: #94a3b8; margin: 5px 0 0 0; font-size: 12px;">Configuration des capteurs</p>
    </div>
""", unsafe_allow_html=True)

# Mode de saisie
mode = st.sidebar.radio("📋 Mode de saisie:", ("Mode Slider", "Mode Formulaire"))

st.sidebar.markdown("### 🎯 Paramètres d'Entrée")

# Sélection du mode
if mode == "Mode Slider":
    st.sidebar.markdown("**🎚️ Ajustez les curseurs**")
    val_humidite = st.sidebar.slider("💧 Humidité (%)", min_value=0.0, max_value=100.0, value=45.5, step=0.1)
    val_temperature = st.sidebar.slider("🌡️ Température (°C)", min_value=-10.0, max_value=50.0, value=24.2, step=0.1)
    val_co2 = st.sidebar.slider("💨 Concentration CO2 (ppm)", min_value=0.0, max_value=5000.0, value=450.0, step=10.0)
    val_o2 = st.sidebar.slider("🫁 Concentration O2 (%vol)", min_value=0.0, max_value=25.0, value=20.9, step=0.1)

else:  # Mode Formulaire
    st.sidebar.markdown("**📝 Entrez les paramètres**")
    col_form1, col_form2 = st.sidebar.columns(2)
    
    with col_form1:
        val_humidite = st.number_input("💧 Humidité (%)", min_value=0.0, max_value=100.0, value=45.5, step=0.1)
        val_temperature = st.number_input("🌡️ Température (°C)", min_value=-10.0, max_value=50.0, value=24.2, step=0.1)
    
    with col_form2:
        val_co2 = st.number_input("💨 CO2 (ppm)", min_value=0, max_value=5000, value=450, step=1)
        val_o2 = st.number_input("🫁 O2 (%vol)", min_value=0.0, max_value=25.0, value=20.9, step=0.1)

st.sidebar.markdown("---")

# Bouton d'analyse
btn_analyser = st.sidebar.button("🚀 Lancer l'Analyse", use_container_width=True, type="primary")

st.sidebar.markdown("---")
st.sidebar.markdown("""
    <div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); padding: 15px; 
                border-radius: 10px; border: 1px solid #334155; margin-top: 30px; text-align: center;">
        <p style="color: #64748b; margin: 0; font-size: 11px;">
            <strong>DataVision AI v2.0</strong><br>
            Prédictions Temps Réel
        </p>
    </div>
""", unsafe_allow_html=True)

# --- CONTENU PRINCIPAL ---

# Variables de résultats
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
        with st.spinner("⏳ Analyse en cours..."):
            response = requests.post("https://datavision-api.onrender.com/predict", json=payload)
            if response.status_code == 200:
                api_result = response.json()
                
                if "status" in api_result and api_result["status"] == "error":
                    st.error(f"⚠️ Erreur : {api_result['message']}")
                else:
                    statut_ia = api_result["statut_environnement"]
                    score_ia = str(api_result["score_prediction"])
                    alerte_txt = api_result["alerte_message"]
                    
                    # Enregistrer la prédiction
                    save_prediction(
                        humidite=val_humidite,
                        temperature=val_temperature,
                        co2=int(val_co2),
                        o2=val_o2,
                        statut=statut_ia,
                        score=f"{score_ia}%",
                        message=alerte_txt
                    )
            else:
                st.error("Erreur de communication avec l'API")
    except Exception as e:
        st.error(f"Erreur de connexion : {e}")

# Afficher les résultats
st.subheader("📊 Résultats de l'Analyse")

# Boîte d'alerte principale
if statut_ia == "Optimal":
    render_alert_box("optimal", "✅ STATUT OPTIMAL", "Classe", score_ia)
elif statut_ia == "Avertissement":
    render_warning_alert(
        "⚠️ AVERTISSEMENT",
        f"{alerte_txt}",
        "Surveillez la situation et ajustez les paramètres si nécessaire"
    )
elif statut_ia == "Critique":
    render_critical_alert(
        "🚨 CRITIQUE",
        f"{alerte_txt}",
        "Intervention immédiate requise : vérifiez la source du problème"
    )
else:
    render_alert_box("info", "🕒 EN ATTENTE", "Statut", "Lancez une analyse pour voir les résultats")

st.markdown("<br>", unsafe_allow_html=True)

# Cartes de métriques
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
        value=f"{int(val_co2)} ppm",
        delta="Normal" if val_co2 <= 1000 else "⚠️ Élevé"
    )

with col4:
    st.metric(
        label="🫁 Oxygène",
        value=f"{val_o2:.1f}%",
        delta="Optimal" if val_o2 >= 19.5 else "⚠️ Bas"
    )

st.markdown("<br><hr>", unsafe_allow_html=True)

# Section graphiques
# Section informations détaillées
st.subheader("ℹ️ Message d'Alerte Détaillé")

st.markdown(f"""
    <div class="card">
        <p style="color: #cbd5e1; margin: 0; line-height: 1.6;">{alerte_txt if btn_analyser else "Lancez une analyse pour obtenir les recommandations."}</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Section recommandations
st.subheader("💡 Recommandations")

recommendations = {
    "Humidité": {
        "value": val_humidite,
        "optimal": (30, 70),
        "advice": "L'humidité idéale se situe entre 30% et 70%"
    },
    "Température": {
        "value": val_temperature,
        "optimal": (20, 26),
        "advice": "La température optimale est entre 20°C et 26°C"
    },
    "CO2": {
        "value": val_co2,
        "optimal": (0, 1000),
        "advice": "Le CO2 doit rester en dessous de 1000 ppm"
    },
    "O2": {
        "value": val_o2,
        "optimal": (19.5, 25),
        "advice": "L'oxygène doit être supérieur à 19.5%"
    }
}

cols_rec = st.columns(2)
for idx, (param, data) in enumerate(recommendations.items()):
    with cols_rec[idx % 2]:
        status = "✅" if data["optimal"][0] <= data["value"] <= data["optimal"][1] else "⚠️"
        st.markdown(f"""
            <div class="card">
                <h4 style="color: #3b82f6; margin: 0 0 10px 0;">{status} {param}</h4>
                <p style="color: #cbd5e1; margin: 0;">{data['advice']}</p>
                <p style="color: #94a3b8; margin: 10px 0 0 0; font-size: 12px;">
                    Intervalle optimal : {data['optimal'][0]} - {data['optimal'][1]}
                </p>
            </div>
        """, unsafe_allow_html=True)

render_footer()
