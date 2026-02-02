"""
Page d'analyse vidéo - Exemple d'extension
À intégrer dans app.py avec un système de pages ou comme module séparé
"""

import streamlit as st
from pathlib import Path
import time

def video_analysis_page():
    """Page dédiée à l'analyse de vidéos"""
    
    st.markdown("""
        <div style='text-align: center; padding: 1.5rem 0;'>
            <h1 style='font-size: 2.5rem; font-weight: 700;'>
                🎬 Analyse vidéo
            </h1>
            <p style='font-size: 1.1rem; color: #666;'>
                Téléchargez une vidéo pour détecter automatiquement le marquage routier
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Section upload
    col_upload, col_info = st.columns([2, 1])
    
    with col_upload:
        st.markdown("### 📤 Téléchargement de vidéo")
        
        uploaded_file = st.file_uploader(
            "Glissez-déposez votre vidéo ou cliquez pour parcourir",
            type=['mp4', 'avi', 'mov', 'mkv'],
            help="Formats acceptés : MP4, AVI, MOV, MKV (max 200MB)"
        )
        
        if uploaded_file:
            st.success(f"✅ Fichier chargé : {uploaded_file.name}")
            
            # Informations fichier
            file_size = uploaded_file.size / (1024 * 1024)  # En MB
            st.info(f"📊 Taille : {file_size:.2f} MB")
            
    with col_info:
        st.markdown("### ℹ️ Recommandations")
        st.markdown("""
            **Qualité optimale** :
            - Résolution : 720p minimum
            - Format : MP4 (H.264)
            - Éclairage : Bon
            - Stabilité : Stable
            
            **Vitesse de capture** :
            - 30-50 km/h recommandé
            - Angle caméra : 45-60°
        """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Paramètres d'analyse
    if uploaded_file:
        st.markdown("### ⚙️ Paramètres d'analyse")
        
        col_p1, col_p2, col_p3 = st.columns(3)
        
        with col_p1:
            confidence = st.slider(
                "Seuil de confiance",
                min_value=0.1,
                max_value=1.0,
                value=0.5,
                step=0.05,
                help="Niveau de confiance minimum pour les détections"
            )
        
        with col_p2:
            detection_classes = st.multiselect(
                "Classes à détecter",
                ["Lignes continues", "Lignes discontinues", "Passages piétons", 
                 "Flèches", "Zones parking", "Texte au sol"],
                default=["Lignes continues", "Lignes discontinues", "Passages piétons"]
            )
        
        with col_p3:
            frame_skip = st.number_input(
                "Images à ignorer",
                min_value=0,
                max_value=10,
                value=2,
                help="Analyser 1 image sur N pour accélérer le traitement"
            )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Bouton de lancement
        col_center = st.columns([1, 2, 1])
        with col_center[1]:
            if st.button("🚀 Lancer l'analyse", use_container_width=True, type="primary"):
                analyze_video(uploaded_file, confidence, detection_classes, frame_skip)

def analyze_video(video_file, confidence, classes, frame_skip):
    """Fonction d'analyse de vidéo (simulation)"""
    
    st.markdown("---")
    st.markdown("### 🔄 Analyse en cours...")
    
    # Étapes d'analyse
    steps = [
        ("Chargement de la vidéo", 10),
        ("Prétraitement des images", 20),
        ("Détection par IA", 50),
        ("Post-traitement", 15),
        ("Génération des résultats", 5)
    ]
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    total_progress = 0
    for step_name, step_weight in steps:
        status_text.markdown(f"**{step_name}...**")
        
        # Simulation du traitement
        for i in range(step_weight):
            time.sleep(0.05)
            total_progress += 1
            progress_bar.progress(total_progress)
    
    status_text.empty()
    progress_bar.empty()
    
    # Résultats
    st.success("✅ Analyse terminée avec succès !")
    
    st.markdown("---")
    st.markdown("### 📊 Résultats de l'analyse")
    
    # Métriques
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    
    col_m1.metric("Objets détectés", "247", "+12%")
    col_m2.metric("Confiance moyenne", "94.3%", "+2.1%")
    col_m3.metric("Temps de traitement", "3.2s", "-0.5s")
    col_m4.metric("Images analysées", "450", "100%")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Détails par classe
    st.markdown("### 🎯 Détections par classe")
    
    col_d1, col_d2 = st.columns(2)
    
    with col_d1:
        st.markdown("""
            <div style='background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);'>
                <h4>Distribution des détections</h4>
        """, unsafe_allow_html=True)
        
        # Données de simulation
        detections_data = {
            "Lignes continues": 89,
            "Lignes discontinues": 76,
            "Passages piétons": 12,
            "Flèches": 34,
            "Zones parking": 28,
            "Texte au sol": 8
        }
        
        for classe, count in detections_data.items():
            st.markdown(f"""
                <div style='margin: 0.8rem 0;'>
                    <div style='display: flex; justify-content: space-between; margin-bottom: 0.3rem;'>
                        <span style='font-weight: 600;'>{classe}</span>
                        <span style='color: #FFA500; font-weight: 700;'>{count}</span>
                    </div>
                    <div style='background: #f0f0f0; height: 8px; border-radius: 4px; overflow: hidden;'>
                        <div style='background: linear-gradient(90deg, #667eea, #FFA500); 
                                    height: 100%; width: {count/max(detections_data.values())*100}%;'></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col_d2:
        st.markdown("""
            <div style='background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);'>
                <h4>Statistiques de qualité</h4>
        """, unsafe_allow_html=True)
        
        quality_metrics = [
            ("Précision globale", "94.3%", "#43e97b"),
            ("Rappel", "91.7%", "#4facfe"),
            ("F1-Score", "92.9%", "#f5576c"),
            ("Temps/frame", "7.1ms", "#FFA500")
        ]
        
        for metric, value, color in quality_metrics:
            st.markdown(f"""
                <div style='background: rgba(0,0,0,0.02); padding: 1rem; 
                            border-radius: 8px; margin: 0.8rem 0; border-left: 4px solid {color};'>
                    <div style='display: flex; justify-content: space-between; align-items: center;'>
                        <span style='font-weight: 600;'>{metric}</span>
                        <span style='font-size: 1.3rem; font-weight: 700; color: {color};'>{value}</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Actions sur les résultats
    st.markdown("### 📥 Exporter les résultats")
    
    col_e1, col_e2, col_e3 = st.columns(3)
    
    with col_e1:
        if st.button("📄 Télécharger le rapport PDF", use_container_width=True):
            st.info("📄 Génération du rapport en cours...")
    
    with col_e2:
        if st.button("📊 Exporter les données CSV", use_container_width=True):
            st.info("📊 Export CSV en cours...")
    
    with col_e3:
        if st.button("🎥 Vidéo annotée", use_container_width=True):
            st.info("🎥 Génération de la vidéo annotée...")

# Pour tester cette page directement
if __name__ == "__main__":
    st.set_page_config(page_title="Analyse Vidéo", page_icon="🎬", layout="wide")
    video_analysis_page()
