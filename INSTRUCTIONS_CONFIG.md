# Instructions pour le fichier config.toml

## Placement du fichier

Le fichier `config.toml` doit être placé dans un dossier `.streamlit` à la racine de votre projet :

```
votre-projet/
├── app.py
├── assets/
│   └── style.css
├── .streamlit/          ← Créez ce dossier
│   └── config.toml      ← Placez le fichier ici
├── requirements.txt
└── README.md
```

## Étapes :

1. **Créez le dossier `.streamlit`** à la racine de votre projet
   - Sur Windows : `mkdir .streamlit`
   - Sur Mac/Linux : `mkdir .streamlit`

2. **Déplacez le fichier `config.toml`** téléchargé dans ce dossier `.streamlit/`

3. **Vérifiez la structure** :
   ```
   .streamlit/
   └── config.toml
   ```

## Pour le déploiement sur Streamlit Cloud :

Streamlit Cloud détectera automatiquement ce fichier et appliquera la configuration.

## Configuration incluse :

- **Thème** : Couleurs personnalisées pour votre application (orange principal)
- **Serveur** : Upload max 200MB, sécurité activée
- **Navigateur** : Désactivation des statistiques d'usage

## Alternative si le dossier `.streamlit` ne fonctionne pas :

Vous pouvez aussi créer un fichier `config.toml` directement sur Streamlit Cloud via l'interface web après déploiement.
