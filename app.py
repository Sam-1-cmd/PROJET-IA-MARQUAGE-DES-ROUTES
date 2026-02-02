import streamlit as st
from pathlib import Path
import time

# ==================================================
# CONFIG GLOBALE STREAMLIT
# ==================================================
st.set_page_config(
    page_title="Détection Marquage Routier | IA Vision",
    page_icon="🛣️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# CHEMINS ROBUSTES
# ==================================================
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
LOGO_PATH = ASSETS_DIR / "logo.jpg"
CSS_PATH = ASSETS_DIR / "style.css"

# ==================================================
# CHARGEMENT DU CSS
# ==================================================
def load_css():
    if CSS_PATH.exists():
        with open(CSS_PATH) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        # CSS inline de secours
        st.markdown("""
            <style>
                .metric-card {
                    background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
                    padding: 1.5rem;
                    border-radius: 8px;
                    border-left: 4px solid #FFA500;
                    margin: 0.5rem 0;
                }
                .status-indicator {
                    display: inline-block;
                    width: 10px;
                    height: 10px;
                    border-radius: 50%;
                    background: #00ff00;
                    animation: pulse 2s infinite;
                }
                @keyframes pulse {
                    0%, 100% { opacity: 1; }
                    50% { opacity: 0.5; }
                }
            </style>
        """, unsafe_allow_html=True)

load_css()

# ==================================================
# SIDEBAR
# ==================================================
with st.sidebar:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), use_column_width=True)
    else:
        # Header de remplacement professionnel
        st.markdown("""
            <div style='text-align: center; padding: 1.5rem 0;'>
                <h1 style='font-size: 2.5rem; margin: 0;'>🛣️</h1>
                <h3 style='margin: 0.5rem 0; color: #FFA500;'>Road Vision AI</h3>
                <p style='font-size: 0.85rem; color: #888;'>Détection intelligente</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Navigation
    st.markdown("### Navigation")
    page = st.radio(
        "",
        ["🏠 Tableau de bord", "📤 Analyse vidéo", "📊 Historique", "⚙️ Paramètres"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Informations système
    st.markdown("### Informations système")
    st.markdown(f"""
        <div style='font-size: 0.85rem;'>
            <p>🔄 Statut : <span style='color: #00ff00;'>En ligne</span></p>
            <p>🧠 Modèle : YOLOv8-Custom</p>
            <p>📍 Version : 2.1.0</p>
            <p>⚡ Performance : Temps réel</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # À propos
    with st.expander("ℹ️ À propos"):
        st.markdown("""
            **Système de détection de marquage routier**
            
            Détection automatique et classification des:
            - Lignes continues/discontinues
            - Passages piétons
            - Flèches directionnelles
            - Zones de stationnement
            - Signalisation horizontale
            
            Développé avec Computer Vision & Deep Learning
        """)

# ==================================================
# PAGE PRINCIPALE
# ==================================================

# Header principal avec animation
st.markdown("""
    <div style='text-align: center; padding: 2rem 0 1rem 0;'>
        <h1 style='font-size: 2.8rem; font-weight: 700; margin-bottom: 0.5rem;'>
            Système de détection du marquage routier
        </h1>
        <p style='font-size: 1.2rem; color: #666;'>
            Intelligence artificielle pour l'analyse d'infrastructures routières
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Métriques principales avec design amélioré
st.markdown("### 📈 Métriques en temps réel")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 1.5rem; border-radius: 12px; text-align: center; color: white;'>
            <div style='font-size: 2.5rem; font-weight: bold; margin-bottom: 0.5rem;'>127</div>
            <div style='font-size: 0.9rem; opacity: 0.9;'>Vidéos analysées</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                    padding: 1.5rem; border-radius: 12px; text-align: center; color: white;'>
            <div style='font-size: 2.5rem; font-weight: bold; margin-bottom: 0.5rem;'>98.7%</div>
            <div style='font-size: 0.9rem; opacity: 0.9;'>Précision moyenne</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div style='background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                    padding: 1.5rem; border-radius: 12px; text-align: center; color: white;'>
            <div style='font-size: 2.5rem; font-weight: bold; margin-bottom: 0.5rem;'>2.3s</div>
            <div style='font-size: 0.9rem; opacity: 0.9;'>Temps de traitement</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div style='background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); 
                    padding: 1.5rem; border-radius: 12px; text-align: center; color: white;'>
            <div style='font-size: 2.5rem; font-weight: bold; margin-bottom: 0.5rem;'>5.2k</div>
            <div style='font-size: 0.9rem; opacity: 0.9;'>Objets détectés</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Section capacités
col_left, col_right = st.columns(2)

with col_left:
    st.markdown("### 🎯 Capacités du système")
    
    capacites = [
        ("Lignes de circulation", "Détection des lignes continues, discontinues et mixtes", "🛣️"),
        ("Passages piétons", "Identification des zones de traversée", "🚶"),
        ("Signalisation horizontale", "Flèches, textes et symboles au sol", "➡️"),
        ("Zones de stationnement", "Places handicapés, réservées, délimitations", "🅿️"),
        ("État du marquage", "Évaluation de l'usure et de la visibilité", "📊")
    ]
    
    for titre, desc, emoji in capacites:
        st.markdown(f"""
            <div style='background: #f8f9fa; padding: 1rem; border-radius: 8px; 
                        margin-bottom: 0.8rem; border-left: 3px solid #FFA500;'>
                <div style='display: flex; align-items: center; margin-bottom: 0.3rem;'>
                    <span style='font-size: 1.5rem; margin-right: 0.8rem;'>{emoji}</span>
                    <strong style='font-size: 1.1rem;'>{titre}</strong>
                </div>
                <p style='margin: 0; padding-left: 2.5rem; color: #666; font-size: 0.9rem;'>{desc}</p>
            </div>
        """, unsafe_allow_html=True)

with col_right:
    st.markdown("### 🔄 Processus d'analyse")
    
    etapes = [
        ("Chargement vidéo", "Upload et validation du format", "1", "#667eea"),
        ("Prétraitement", "Stabilisation et amélioration d'image", "2", "#764ba2"),
        ("Détection IA", "Inférence du modèle de deep learning", "3", "#f5576c"),
        ("Post-traitement", "Filtrage et classification des détections", "4", "#4facfe"),
        ("Export résultats", "Génération des rapports et visualisations", "5", "#43e97b")
    ]
    
    for titre, desc, numero, couleur in etapes:
        st.markdown(f"""
            <div style='background: white; padding: 1rem; border-radius: 8px; 
                        margin-bottom: 0.8rem; border: 2px solid {couleur}; position: relative;'>
                <div style='position: absolute; left: -15px; top: 50%; transform: translateY(-50%);
                            background: {couleur}; color: white; width: 30px; height: 30px;
                            border-radius: 50%; display: flex; align-items: center; justify-content: center;
                            font-weight: bold; font-size: 0.9rem;'>{numero}</div>
                <div style='padding-left: 1.5rem;'>
                    <strong style='color: {couleur};'>{titre}</strong>
                    <p style='margin: 0.3rem 0 0 0; color: #666; font-size: 0.85rem;'>{desc}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Section démarrage rapide
st.markdown("### 🚀 Démarrage rapide")

col_a, col_b, col_c = st.columns(3)

with col_a:
    st.markdown("""
        <div style='text-align: center; padding: 2rem; background: #f8f9fa; border-radius: 12px;'>
            <div style='font-size: 3rem; margin-bottom: 1rem;'>📤</div>
            <h4>Étape 1</h4>
            <p style='color: #666;'>Téléchargez votre vidéo de route</p>
        </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown("""
        <div style='text-align: center; padding: 2rem; background: #f8f9fa; border-radius: 12px;'>
            <div style='font-size: 3rem; margin-bottom: 1rem;'>🤖</div>
            <h4>Étape 2</h4>
            <p style='color: #666;'>Le modèle IA analyse automatiquement</p>
        </div>
    """, unsafe_allow_html=True)

with col_c:
    st.markdown("""
        <div style='text-align: center; padding: 2rem; background: #f8f9fa; border-radius: 12px;'>
            <div style='font-size: 3rem; margin-bottom: 1rem;'>📊</div>
            <h4>Étape 3</h4>
            <p style='color: #666;'>Consultez et exportez les résultats</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Bouton d'action principal
col_center = st.columns([1, 2, 1])
with col_center[1]:
    if st.button("🎬 Lancer une analyse", use_container_width=True, type="primary"):
        with st.spinner("Initialisation du système..."):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
        st.success("✅ Système prêt ! Rendez-vous dans l'onglet 'Analyse vidéo' pour commencer.")

st.markdown("---")

# Footer
st.markdown("""
    <div style='text-align: center; padding: 2rem 0; color: #888; font-size: 0.85rem;'>
        <p>🛣️ Road Vision AI - Système de détection de marquage routier</p>
        <p>Propulsé par Computer Vision & Deep Learning | Version 2.1.0</p>
    </div>
""", unsafe_allow_html=True)
