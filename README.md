# News_automation
Ce repo contient le code d'un algo Python qui recupere differentes informations comme la méteo les news et les tendances crypto journaliere et en fais un document recap qu'il envoie de facon automatisé par mail.

# 📰 Daily News Aggregator

Un agrégateur de news quotidien qui collecte automatiquement des informations sur la météo, les actualités et les cryptomonnaies, puis envoie un résumé par email.

## 🚀 Fonctionnalités

- 🌤️ **Météo** : Conditions météorologiques actuelles
- 📰 **Actualités** : Articles tendances du jour  
- ₿ **Cryptomonnaies** : Prix et variations des principales cryptos
- 📧 **Email quotidien** : Résumé formaté envoyé automatiquement
- ⏰ **Planification** : Exécution automatique chaque jour à 8h00

## 🛠️ Stack Technique

- **Python 3.8+** - Langage principal
- **APIs** : OpenWeatherMap, NewsAPI, CoinGecko
- **Email** : SMTP via Gmail
- **Planification** : Bibliothèque schedule

## 📦 Installation

### 1. Cloner le repository
```bash
git clone https://github.com/votre-username/daily-news-aggregator.git
cd daily-news-aggregator
2. Installer les dépendances
bash
pip install -r requirements.txt```

3. Configuration des APIs
🔑 OpenWeatherMap
Créer un compte sur OpenWeatherMap
```
# Obtenir une clé API gratuite

Ajouter la clé dans le fichier .env

#  NewsAPI
S'inscrire sur NewsAPI

Générer une clé API

Ajouter la clé dans le fichier .env

₿ CoinGecko
✅ Aucune clé requise ! L'API est libre d'accès.

# Configuration Gmail
Activer la validation en 2 étapes

Générer un mot de passe d'application

Utiliser ce mot de passe dans le fichier .env

# Configuration de l'environnement
Copier le fichier .env.example vers .env :

bash
cp .env.example .env
Editer le fichier .env avec vos paramètres :

env
# Clés APIs
WEATHER_API_KEY=votre_cle_openweathermap_ici
NEWS_API_KEY=votre_cle_newsapi_ici

# Configuration Email
EMAIL_SENDER=votre.email@gmail.com
EMAIL_PASSWORD=votre_mot_de_passe_application_gmail
EMAIL_RECEIVER=destinataire@email.com

# Configuration Géographique
CITY=Paris
COUNTRY=FR

# Configuration Crypto
CRYPTO_IDS=bitcoin,ethereum,cardano
CRYPTO_CURRENCY=eur
🎯 Utilisation

# Lancer manuellement
bash
python main.py
Exécution automatique (Recommandé)
Le système est conçu pour tourner en continu et envoyer un email chaque jour à 8h00.

Pour une utilisation en production, utilisez un planificateur de tâches :

Sur Linux/Mac (cron)
bash
# Éditer la crontab
crontab -e

# Ajouter cette ligne pour exécution quotidienne à 8h00
0 8 * * * /usr/bin/python3 /chemin/vers/daily-news-aggregator/main.py
Sur Windows (Task Scheduler)
Créer une tâche planifiée qui exécute main.py quotidiennement.

# Structure du Projet
text
daily-news-aggregator/
├── config/
│   └── config.py          # Configuration centrale
├── services/
│   ├── crypto_service.py  # Service cryptomonnaies
│   ├── weather_service.py # Service météo
│   ├── news_service.py    # Service actualités
│   └── email_service.py   # Service email
├── templates/             # Templates HTML (futur)
├── tests/                 # Tests unitaires (futur)
├── .env                   # Variables d'environnement ⚠️ NE PAS PARTAGER
├── .env.example           # Template de configuration
├── requirements.txt       # Dépendances Python
├── main.py               # Point d'entrée
└── README.md             # Ce fichier

# Développement
Architecture
Le projet suit une architecture modulaire :

Services : Chaque source de données a son propre service

Configuration centralisée : Tous les paramètres dans config.py

Gestion d'erreurs : Chaque service gère ses propres erreurs

Sécurité : Clés API stockées dans .env

Ajouter une   nouvelle source
Créer un nouveau fichier dans services/

Implémenter une fonction qui retourne une liste de dictionnaires

Modifier main.py pour inclure la nouvelle source

Mettre à jour la configuration si nécessaire

Tests
bash
# Tester la configuration
python test_config.py

# Tester le service crypto
python test_crypto.py

# Tester l'email avec des données mock
python test_email.py
🐛 Dépannage
Erreurs courantes
❌ "ModuleNotFoundError: No module named 'config'"

Vérifier la structure des dossiers

S'assurer que config/ est un dossier, pas un fichier

❌ "Invalid API Key"

Vérifier que les clés dans .env sont correctes

S'assurer qu'il n'y a pas d'espaces avant/après

❌ Erreur d'authentification Gmail

Vérifier que la validation en 2 étapes est activée

Utiliser un mot de passe d'application, pas le mot de passe principal

❌ "API rate limit exceeded"

Attendre quelques minutes avant de réessayer

Vérifier les limites de l'API utilisée

📈 Améliorations Futures
Interface web de configuration

Base de données pour l'historique

Plus de sources de news

Templates email personnalisables

Système de logs avancé

Tests unitaires complets

Dockerisation

🤝 Contribution
Les contributions sont les bienvenues ! N'hésitez pas à :

Fork le projet

Créer une branche pour votre fonctionnalité

Commiter vos changements

Ouvrir une Pull Request

📄 Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

🙏 Remerciements
OpenWeatherMap pour les données météo

NewsAPI pour les actualités

CoinGecko pour les données cryptomonnaies

Développé avec ❤️ et Python

text

## 📁 Fichiers Supplémentaires à Créer

### **1. `.env.example`**
```env
# Configuration des APIs
WEATHER_API_KEY=votre_cle_openweathermap_ici
NEWS_API_KEY=votre_cle_newsapi_ici

# Configuration Email
EMAIL_SENDER=votre.email@gmail.com
EMAIL_PASSWORD=votre_mot_de_passe_application_gmail
EMAIL_RECEIVER=destinataire@email.com

# Configuration Géographique
CITY=Paris
COUNTRY=FR

# Configuration Crypto
CRYPTO_IDS=bitcoin,ethereum,cardano
CRYPTO_CURRENCY=eur
CRYPTO_LIMIT=2

# Configuration Actualités
NEWS_COUNTRY=fr
NEWS_PAGE_SIZE=2

# Configuration Planification
SCHEDULE_TIME=08:00
2. .gitignore
gitignore
# Environment variables
.env
.env.local

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
venv/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
🚀 Commandes pour Créer le Repo GitHub
bash
# Initialiser Git
git init

# Ajouter tous les fichiers
git add .

# Premier commit
git commit -m "Initial commit: Daily News Aggregator MVP"

# Créer le repo sur GitHub (manuellement via l'interface web)
# Puis lier le repo local au remote
git remote add origin https://github.com/votre-username/daily-news-aggregator.git

# Pousser le code
git branch -M main
git push -u origin main