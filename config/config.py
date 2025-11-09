import os
from dotenv import load_dotenv

# Charge les variables du fichier .env
load_dotenv()

class Config:
    """
    Configuration centrale de l'application
    Tous les paramètres viennent du fichier .env
    """
    
    # 🔑 API Keys (Météo et Actualités)
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
    NEWS_API_KEY = os.getenv('NEWS_API_KEY')
    # Pas de clé pour Crypto (CoinGecko) 🎉
    
    # 📧 Configuration Email
    EMAIL_SENDER = os.getenv('EMAIL_SENDER')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER')
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')  # Valeur par défaut
    SMTP_PORT = int(os.getenv('SMTP_PORT', 587))              # Conversion en nombre
    
    # 🌍 Configuration Géographique
    CITY = os.getenv('CITY', 'Paris')
    COUNTRY = os.getenv('COUNTRY', 'FR')
    
    # 📰 Configuration Actualités
    NEWS_COUNTRY = os.getenv('NEWS_COUNTRY', 'fr')
    NEWS_PAGE_SIZE = int(os.getenv('NEWS_PAGE_SIZE', 2))
    
    # ₿ Configuration Crypto
    CRYPTO_IDS = os.getenv('CRYPTO_IDS', 'bitcoin,ethereum,solana')
    CRYPTO_CURRENCY = os.getenv('CRYPTO_CURRENCY', 'eur')
    CRYPTO_LIMIT = int(os.getenv('CRYPTO_LIMIT', 2))
    
    # ⏰ Configuration Planification
    SCHEDULE_TIME = os.getenv('SCHEDULE_TIME', '08:00')
    
    # 🔗 URLs des APIs
    WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
    NEWS_URL = "https://newsapi.org/v2/top-headlines"
    CRYPTO_URL = "https://api.coingecko.com/api/v3/coins/markets"