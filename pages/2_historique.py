import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta
from utils import apply_global_styles, render_header, render_card, render_footer

# Configuration
if __name__ == "__main__":
    st.set_page_config(page_title="Historique - DataVision", layout="wide")
apply_global_styles()

# Header
render_header("📊 Historique des Prédictions", "Consultez et analysez l'historique de vos prédictions")

# --- CONTRÔLES ---
st.subheader("🔍 Filtres et Options")

col_filter1, col_filter2, col_filter3 = st.columns(3)

with col_filter1:
    date_from = st.date_input("Date de début", value=datetime.now() - timedelta(days=30))

with col_filter2:
    date_to = st.date_input("Date de fin", value=datetime.now())

with col_filter3:
    statut_filter = st.selectbox("Filtrer par statut", ["Tous", "Optimal", "Avertissement", "Critique"])

# --- GÉNÉRER DES DONNÉES D'EXEMPLE ---
# Créer un historique d'exemple
@st.cache_data
def generate_sample_data():
    data = []
    statuts = ["Optimal", "Avertissement", "Critique", "Optimal", "Optimal", "Avertissement"]
    
    for i in range(50):
        date = datetime.now() - timedelta(days=random.randint(0, 30))
        data.append({
            "ID": f"#2026050{i:03d}",
            "Date/Heure": date.strftime("%Y-%m-%d %H:%M:%S"),
            "Humidité (%)": round(random.uniform(20, 80), 1),
            "Température (°C)": round(random.uniform(15, 30), 1),
            "CO2 (ppm)": random.randint(300, 2000),
            "O2 (%vol)": round(random.uniform(18, 21), 1),
            "Statut": random.choice(statuts),
            "Précision": f"{random.randint(85, 99)}%"
        })
    
    return pd.DataFrame(data)

df_historique = generate_sample_data()

# Filtrer les données
if statut_filter != "Tous":
    df_filtree = df_historique[df_historique["Statut"] == statut_filter]
else:
    df_filtree = df_historique.copy()

# --- STATISTIQUES GÉNÉRALES ---
st.subheader("📈 Statistiques Globales")

col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)

with col_stat1:
    st.metric(
        label="📊 Total Analyses",
        value=len(df_filtree),
        delta=f"Filtrées : {len(df_filtree)}/{len(df_historique)}"
    )

with col_stat2:
    optimal_count = len(df_filtree[df_filtree["Statut"] == "Optimal"])
    st.metric(
        label="✅ Optimal",
        value=optimal_count,
        delta=f"{(optimal_count/len(df_filtree)*100):.1f}%" if len(df_filtree) > 0 else "N/A"
    )

with col_stat3:
    warning_count = len(df_filtree[df_filtree["Statut"] == "Avertissement"])
    st.metric(
        label="⚠️ Avertissement",
        value=warning_count,
        delta=f"{(warning_count/len(df_filtree)*100):.1f}%" if len(df_filtree) > 0 else "N/A"
    )

with col_stat4:
    critical_count = len(df_filtree[df_filtree["Statut"] == "Critique"])
    st.metric(
        label="🚨 Critique",
        value=critical_count,
        delta=f"{(critical_count/len(df_filtree)*100):.1f}%" if len(df_filtree) > 0 else "N/A"
    )

st.markdown("<br>", unsafe_allow_html=True)

# --- TABLEAU HISTORIQUE ---
st.subheader("📋 Détail des Prédictions")

# Coloriser le tableau
def color_statut(val):
    if val == "Optimal":
        return "background-color: rgba(16, 185, 129, 0.2); color: #10b981;"
    elif val == "Avertissement":
        return "background-color: rgba(245, 158, 11, 0.2); color: #f59e0b;"
    elif val == "Critique":
        return "background-color: rgba(239, 68, 68, 0.2); color: #ef4444;"
    return ""

styled_df = df_filtree.style.applymap(
    lambda x: color_statut(x) if isinstance(x, str) and x in ["Optimal", "Avertissement", "Critique"] else ""
)

st.dataframe(styled_df, use_container_width=True, height=400)

# Option de téléchargement
col_dl1, col_dl2 = st.columns([1, 4])

with col_dl1:
    csv = df_filtree.to_csv(index=False)
    st.download_button(
        label="📥 Télécharger CSV",
        data=csv,
        file_name=f"datavision_historique_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )

st.markdown("<br><hr>", unsafe_allow_html=True)

# --- GRAPHIQUES STATISTIQUES ---
st.subheader("📊 Tendances et Analyses")

col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.markdown("<h4 style='color: #3b82f6;'>Distribution des Statuts</h4>", unsafe_allow_html=True)
    statut_counts = df_filtree["Statut"].value_counts()
    st.bar_chart(statut_counts)

with col_chart2:
    st.markdown("<h4 style='color: #3b82f6;'>Moyenne Humidité par Jour</h4>", unsafe_allow_html=True)
    humidite_par_jour = df_filtree.groupby(df_filtree["Date/Heure"].str[:10])["Humidité (%)"].mean()
    st.line_chart(humidite_par_jour)

st.markdown("<br>", unsafe_allow_html=True)

col_chart3, col_chart4 = st.columns(2)

with col_chart3:
    st.markdown("<h4 style='color: #3b82f6;'>Moyenne Température par Jour</h4>", unsafe_allow_html=True)
    temp_par_jour = df_filtree.groupby(df_filtree["Date/Heure"].str[:10])["Température (°C)"].mean()
    st.line_chart(temp_par_jour)

with col_chart4:
    st.markdown("<h4 style='color: #3b82f6;'>Distribution CO2</h4>", unsafe_allow_html=True)
    st.bar_chart(df_filtree["CO2 (ppm)"].describe())

st.markdown("<br>", unsafe_allow_html=True)

# --- INSIGHTS DÉTAILLÉS ---
st.subheader("💡 Insights et Observations")

col_insight1, col_insight2 = st.columns(2)

with col_insight1:
    avg_humidite = df_filtree["Humidité (%)"].mean()
    render_card(
        "💧 Humidité Moyenne",
        f"La moyenne d'humidité est de <strong>{avg_humidite:.1f}%</strong>. "
        f"{'Conditions optimales' if 30 <= avg_humidite <= 70 else 'À surveiller'}"
    )

with col_insight2:
    avg_temp = df_filtree["Température (°C)"].mean()
    render_card(
        "🌡️ Température Moyenne",
        f"La température moyenne est de <strong>{avg_temp:.1f}°C</strong>. "
        f"{'Confortable' if 20 <= avg_temp <= 26 else 'À réguler'}"
    )

col_insight3, col_insight4 = st.columns(2)

with col_insight3:
    avg_co2 = df_filtree["CO2 (ppm)"].mean()
    render_card(
        "💨 CO2 Moyen",
        f"La concentration CO2 moyenne est de <strong>{avg_co2:.0f} ppm</strong>. "
        f"{'Normal' if avg_co2 <= 1000 else 'Élevé'}"
    )

with col_insight4:
    avg_o2 = df_filtree["O2 (%vol)"].mean()
    render_card(
        "🫁 Oxygène Moyen",
        f"La concentration O2 moyenne est de <strong>{avg_o2:.1f}%</strong>. "
        f"{'Optimal' if avg_o2 >= 19.5 else 'Bas'}"
    )

st.markdown("<br>", unsafe_allow_html=True)

# --- TABLEAUX RÉCAPITULATIFS ---
st.subheader("📋 Récapitulatifs par Paramètre")

tab1, tab2, tab3, tab4 = st.tabs(["Humidité", "Température", "CO2", "O2"])

with tab1:
    hum_stats = df_filtree["Humidité (%)"].describe()
    st.dataframe(hum_stats.to_frame().T)

with tab2:
    temp_stats = df_filtree["Température (°C)"].describe()
    st.dataframe(temp_stats.to_frame().T)

with tab3:
    co2_stats = df_filtree["CO2 (ppm)"].describe()
    st.dataframe(co2_stats.to_frame().T)

with tab4:
    o2_stats = df_filtree["O2 (%vol)"].describe()
    st.dataframe(o2_stats.to_frame().T)

render_footer()
