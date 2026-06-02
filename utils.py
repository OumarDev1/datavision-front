import streamlit as st

def apply_global_styles():
    """Applique les styles CSS globaux à toutes les pages"""
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
        div[data-testid="stMetricBlock"]:nth-of-type(1) { border-left-color: #3b82f6 !important; }
        div[data-testid="stMetricBlock"]:nth-of-type(2) { border-left-color: #f59e0b !important; }
        div[data-testid="stMetricBlock"]:nth-of-type(3) { border-left-color: #ef4444 !important; }
        div[data-testid="stMetricBlock"]:nth-of-type(4) { border-left-color: #10b981 !important; }
        
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
        
        h3 {
            color: #cbd5e1 !important;
            font-weight: 600 !important;
        }
        
        /* Messages d'alerte stylisés */
        .stSuccess, .stWarning, .stError, .stInfo {
            border-radius: 12px !important;
            border-left: 5px solid !important;
            padding: 20px !important;
            font-weight: 500 !important;
        }
        
        /* Cartes personnalisées */
        .card {
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            padding: 25px;
            border-radius: 12px;
            border: 1px solid #334155;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
        }
        
        .card:hover {
            box-shadow: 0 12px 24px rgba(59, 130, 246, 0.2);
            border-color: #3b82f6;
            transition: all 0.3s ease;
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

def render_header(title: str, subtitle: str):
    """Affiche un header standard"""
    st.markdown(f"""
        <div class="header-main">
            <div class="header-title">{title}</div>
            <div class="header-subtitle">{subtitle}</div>
        </div>
    """, unsafe_allow_html=True)

def render_alert_box(status: str, title: str, subtitle: str, message: str):
    """Affiche une boîte d'alerte stylisée"""
    colors = {
        "optimal": {"bg": "#064e3b", "border": "#10b981", "text": "#d1fae5"},
        "warning": {"bg": "#78350f", "border": "#f59e0b", "text": "#fef3c7"},
        "critical": {"bg": "#7f1d1d", "border": "#ef4444", "text": "#fee2e2"},
        "info": {"bg": "#0c4a6e", "border": "#3b82f6", "text": "#bae6fd"}
    }
    
    color = colors.get(status, colors["info"])
    
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, {color['bg']} 0%, {color['bg']} 100%); 
                    padding: 25px; border-radius: 12px; border-left: 5px solid {color['border']}; 
                    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);">
            <h3 style="color: {color['border']}; margin: 0 0 10px 0;">{title}</h3>
            <p style="color: {color['text']}; margin: 0; font-size: 15px;"><strong>{subtitle}:</strong> {message}</p>
        </div>
    """, unsafe_allow_html=True)

def render_warning_alert(title: str, message: str, action: str):
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #7c2d12 0%, #92400e 100%); 
                    padding: 28px; border-radius: 14px; border-left: 6px solid #f59e0b; 
                    box-shadow: 0 10px 22px rgba(249, 115, 22, 0.18);">
            <h3 style="color: #f59e0b; margin: 0 0 12px 0;">{title}</h3>
            <p style="color: #fde68a; margin: 0 0 10px 0; font-size: 15px;">{message}</p>
            <p style="color: #f8d5a3; margin: 0; font-size: 14px; font-weight: 600;">Action recommandée : {action}</p>
        </div>
    """, unsafe_allow_html=True)

def render_critical_alert(title: str, message: str, action: str):
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #7f1d1d 0%, #991b1b 100%); 
                    padding: 28px; border-radius: 14px; border-left: 6px solid #ef4444; 
                    box-shadow: 0 10px 22px rgba(239, 68, 68, 0.30);">
            <h3 style="color: #fca5a5; margin: 0 0 12px 0;">{title}</h3>
            <p style="color: #fee2e2; margin: 0 0 10px 0; font-size: 15px;">{message}</p>
            <p style="color: #fee2e2; margin: 0; font-size: 14px; font-weight: 700;">Action urgente : {action}</p>
        </div>
    """, unsafe_allow_html=True)

def render_card(title: str, content: str):
    """Affiche une carte personnalisée"""
    st.markdown(f"""
        <div class="card">
            <h3 style="color: #3b82f6; margin: 0 0 15px 0;">{title}</h3>
            <p style="color: #cbd5e1; margin: 0;">{content}</p>
        </div>
    """, unsafe_allow_html=True)

def render_footer():
    """Affiche un footer standard"""
    st.markdown("""
        <hr>
        <div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); padding: 20px; 
                    border-radius: 12px; border-left: 4px solid #3b82f6; margin-top: 40px; text-align: center;">
            <p style="color: #64748b; margin: 0; font-size: 12px;">
                🔄 DataVision AI Platform v2.0 | 📡 Connexion API : Active | 🤖 Modèle : Random Forest
            </p>
            <p style="color: #475569; margin: 5px 0 0 0; font-size: 11px;">
                © 2026 DataVision. Tous droits réservés.
            </p>
        </div>
    """, unsafe_allow_html=True)
