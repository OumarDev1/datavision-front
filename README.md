# 🌐 DataVision AI Platform v2.0

Plateforme intelligente de prédiction environnementale basée sur le Machine Learning (Random Forest).

## 📋 Table des matières

- [Fonctionnalités](#fonctionnalités)
- [Architecture](#architecture)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Pages disponibles](#pages-disponibles)
- [Configuration](#configuration)

## ✨ Fonctionnalités

### 🔮 Prédictions en Temps Réel
- **Mode Slider** : Interface intuitive avec curseurs pour ajustements rapides
- **Mode Formulaire** : Saisie précise des paramètres
- Analyse instantanée basée sur le modèle Random Forest
- Messages d'alerte détaillés et personnalisés

### 📊 Historique Complet
- Consultation de toutes les analyses précédentes
- Filtrage par date et par statut
- Statistiques détaillées et tendances
- Export en CSV pour analyse externe

### ⚙️ Configuration Avancée
- Personnalisation des seuils d'alerte
- Configuration de l'API
- Gestion des notifications
- Préférences visuelles et intégrations

### 📚 Documentation Interactive
- Guide complet d'utilisation
- FAQ détaillées
- Architecture API
- Support et contacte

## 🏗️ Architecture

```
datavision-front/
├── app.py                          # Page d'accueil (Dashboard)
├── utils.py                        # Fonctions partagées et styles
├── requirements.txt                # Dépendances Python
├── pages/
│   ├── 1_🔮_Prediction.py         # Centre de prédictions
│   ├── 2_📊_Historique.py         # Historique des analyses
│   ├── 3_⚙️_Configuration.py       # Paramètres de la plateforme
│   └── 4_📚_Documentation.py      # Guide et documentation
└── README.md                       # Ce fichier
```

## 📥 Installation

### Prérequis
- Python 3.8+
- pip ou conda
- Connexion internet (pour l'API)

### Étapes

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
venv\Scripts\activate  # Windows
```

3. **Installez les dépendances**
```bash
pip install -r requirements.txt
```

4. **Lancez l'application**
```bash
streamlit run app.py
```

5. **Accédez à l'application**
```
Ouvrez votre navigateur à : http://localhost:8501
```

## 🚀 Utilisation Rapide

### Première Analyse

1. **Accédez à la page "🔮 Prédictions"** depuis le menu latéral
2. **Choisissez un mode** :
   - Mode Slider pour une interface rapide
   - Mode Formulaire pour une saisie précise
3. **Entrez les paramètres** de vos capteurs
4. **Cliquez sur "🚀 Lancer l'Analyse"**
5. **Consultez les résultats** et recommandations

### Consulter l'Historique

1. **Accédez à la page "📊 Historique"**
2. **Appliquez des filtres** (date, statut)
3. **Consultez les statistiques** et tendances
4. **Téléchargez les données** en CSV si nécessaire

## 📄 Pages Disponibles

### 🏠 Accueil (Dashboard)
- Vue d'ensemble de la plateforme
- Statistiques globales
- Guide de démarrage rapide
- Informations sur les fonctionnalités

### 🔮 Prédictions
- Saisie des paramètres (2 modes)
- Analyse en temps réel
- Résultats avec statut et score
- Visualisations et recommandations
- Graphiques de tendance

### 📊 Historique
- Liste complète des analyses
- Filtrage avancé
- Statistiques par paramètre
- Export des données
- Graphiques de tendance

### ⚙️ Configuration
- Configuration de l'API
- Seuils d'alerte personnalisables
- Préférences visuelles
- Gestion des notifications
- Intégrations (Email, Slack, Webhooks)

### 📚 Documentation
- Guide d'installation
- Guide d'utilisation détaillé
- Architecture API
- FAQ complètes
- Support et contacte

## ⚙️ Configuration

### Seuils d'Alerte par Défaut

| Paramètre | Minimum | Maximum | Unité |
|-----------|---------|---------|-------|
| Humidité | 30 | 70 | % |
| Température | 20 | 26 | °C |
| CO2 | - | 1000 | ppm |
| O2 | 19.5 | - | %vol |

### Personnaliser les Seuils

1. Allez à la page **⚙️ Configuration**
2. Section **⚠️ Seuils d'Alerte**
3. Ajustez les curseurs selon vos besoins
4. Cliquez sur **Sauvegarder les paramètres**

## 📊 Paramètres Environnementaux

### 💧 Humidité
- **Plage normale** : 30% - 70%
- **Trop basse** : Risque de sécheresse
- **Trop élevée** : Risque de moisissures

### 🌡️ Température
- **Plage optimale** : 20°C - 26°C
- **Trop basse** : Inconfort thermique
- **Trop élevée** : Consommation énergétique

### 💨 Dioxyde de Carbone (CO2)
- **Normal** : < 800 ppm
- **Attention** : 800-1200 ppm
- **Critique** : > 1200 ppm

### 🫁 Oxygène (O2)
- **Plage normale** : 19.5% - 21%
- **Bas** : < 19.5% (dangereux)
- **Optimal** : 19.5% - 21%

## 🔗 API

### Endpoint de Prédiction

**URL:** `POST https://datavision-api.onrender.com/predict`

**Paramètres (JSON):**
```json
{
    "humidite": 45.5,
    "temperature": 24.2,
    "co2": 450,
    "o2": 20.9
}
```

**Réponse:**
```json
{
    "statut_environnement": "Optimal",
    "score_prediction": 1,
    "alerte_message": "Conditions optimales maintenues..."
}
```

## 🎨 Design et Styles

- **Thème** : Mode sombre moderne
- **Couleurs principales** : Bleu (#3b82f6), Blanc, Gris
- **Animations** : Transitions fluides et fade-in
- **Responsive** : Adapté à tous les écrans

## 📦 Dépendances

```
streamlit>=1.28.0
requests>=2.31.0
pandas>=2.0.0
```

Voir `requirements.txt` pour la liste complète.

## 🔧 Dépannage

### L'application ne démarre pas
- Vérifiez que Streamlit est installé : `pip install streamlit`
- Vérifiez le port 8501 n'est pas utilisé
- Relancez avec : `streamlit run app.py`

### L'API ne répond pas
- Vérifiez votre connexion internet
- Vérifiez l'URL de l'API en Configuration
- Vérifiez les paramètres envoyés

### Données manquantes
- Vérifiez les seuils d'alerte configurés
- Vérifiez la date de conservation des données
- Consultez l'historique filtré

## 📞 Support

- **Email** : support@datavision.com
- **Chat** : Disponible sur la plateforme
- **Documentation** : docs.datavision.com
- **FAQ** : Page Documentation > FAQ

## 📈 Versioning

- **Version actuelle** : 2.0
- **Date de sortie** : Mai 2026
- **Modèle IA** : Random Forest

## 📄 Licence

© 2026 DataVision. Tous droits réservés.

## 🎯 Roadmap Futur

- [ ] Support de multiples modèles IA
- [ ] Intégration IoT avancée
- [ ] Alertes SMS
- [ ] Interface mobile native
- [ ] API REST complète
- [ ] Dashboard personnalisable
- [ ] Prédictions long terme
- [ ] Machine learning amélioré

---

**Merci d'utiliser DataVision AI Platform !** 🚀
