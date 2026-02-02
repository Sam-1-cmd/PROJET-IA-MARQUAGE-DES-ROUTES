# 🛣️ Road Vision AI - Système de détection de marquage routier

Interface professionnelle Streamlit pour la détection intelligente du marquage routier par intelligence artificielle.

## 🚀 Fonctionnalités

- **Détection multi-classes** : lignes de circulation, passages piétons, flèches, zones de stationnement
- **Interface moderne** : Design professionnel adapté au secteur des infrastructures routières
- **Temps réel** : Analyse vidéo performante avec visualisation instantanée
- **Export de données** : Génération de rapports et statistiques détaillées
- **Visualisations** : Graphiques et métriques pour le suivi de la qualité

## 📋 Prérequis

```bash
python >= 3.8
streamlit >= 1.28.0
```

## 🛠️ Installation

1. **Cloner le projet**
```bash
git clone <votre-repo>
cd road-vision-ai
```

2. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

3. **Structure des fichiers**
```
project/
├── app.py                 # Application Streamlit principale
├── assets/
│   ├── style.css         # Feuille de style personnalisée
│   └── logo.jpg          # Logo (optionnel)
├── requirements.txt      # Dépendances Python
└── README.md            # Ce fichier
```

## 🎯 Lancement local

```bash
streamlit run app.py
```

L'application sera accessible sur `http://localhost:8501`

## ☁️ Déploiement sur Streamlit Cloud

### Méthode 1 : Via l'interface web

1. Poussez votre code sur GitHub
2. Connectez-vous sur [share.streamlit.io](https://share.streamlit.io)
3. Cliquez sur "New app"
4. Sélectionnez votre repository, branche et fichier `app.py`
5. Cliquez sur "Deploy"

### Méthode 2 : Via la CLI

```bash
# Installer streamlit CLI
pip install streamlit

# Se connecter
streamlit login

# Déployer
streamlit deploy app.py
```

## 📦 requirements.txt

Créez un fichier `requirements.txt` avec :

```txt
streamlit==1.30.0
Pillow==10.1.0
numpy==1.24.3
opencv-python-headless==4.8.1.78
```

## ⚙️ Configuration

### Variables d'environnement (optionnel)

Créez un fichier `.streamlit/config.toml` :

```toml
[theme]
primaryColor = "#FFA500"
backgroundColor = "#f5f7fa"
secondaryBackgroundColor = "#ffffff"
textColor = "#1a1a1a"
font = "sans serif"

[server]
maxUploadSize = 200
enableXsrfProtection = true
```

## 🎨 Personnalisation

### Modifier les couleurs

Éditez les variables CSS dans `assets/style.css` :

```css
:root {
    --primary-color: #FFA500;     /* Couleur principale */
    --accent-color: #667eea;      /* Couleur d'accent */
    --success-color: #43e97b;     /* Couleur de succès */
}
```

### Ajouter votre logo

Placez votre logo dans `assets/logo.jpg` ou modifiez le chemin dans `app.py`.

## 🔧 Intégration de votre modèle IA

Pour intégrer votre modèle de détection, remplacez la section démo dans `app.py` :

```python
# Exemple d'intégration YOLOv8
from ultralytics import YOLO

@st.cache_resource
def load_model():
    return YOLO('votre_modele.pt')

model = load_model()

# Dans la fonction d'analyse
results = model(video_frame)
```

## 📊 Structure de l'interface

- **Sidebar** : Navigation, informations système, paramètres
- **Dashboard** : Métriques temps réel, capacités du système
- **Analyse vidéo** : Upload et traitement des vidéos
- **Historique** : Consultations des analyses précédentes
- **Paramètres** : Configuration du système

## 🐛 Résolution des problèmes

### Le CSS ne se charge pas
- Vérifiez que `assets/style.css` existe
- Utilisez des chemins absolus avec `Path`

### Erreur de déploiement Streamlit
- Vérifiez que `requirements.txt` est à jour
- Assurez-vous que tous les fichiers sont commités sur Git
- Vérifiez les logs dans Streamlit Cloud

### Performance lente
- Utilisez `@st.cache_resource` pour le chargement du modèle
- Utilisez `@st.cache_data` pour les données
- Limitez la résolution vidéo pour le traitement

## 📝 TODO / Améliorations futures

- [ ] Ajout de l'analyse en temps réel via webcam
- [ ] Export des résultats en CSV/JSON
- [ ] Graphiques interactifs avec Plotly
- [ ] Système d'authentification
- [ ] Base de données pour l'historique
- [ ] API REST pour intégration externe
- [ ] Support multi-langues

## 📄 Licence

Projet développé pour la détection de marquage routier.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir des issues ou des pull requests.

## 📧 Contact

Pour toute question ou suggestion concernant le projet.

---

**Note** : Cette interface est conçue pour être intégrée avec un modèle de Computer Vision. Les fonctionnalités d'analyse nécessitent l'implémentation de votre modèle spécifique.
