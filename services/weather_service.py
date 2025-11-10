import requests
from config.config import Config

def get_weather_news():
    """
    Récupère les informations météo depuis OpenWeatherMap
    Retourne une liste avec les données météo formatées
    """
    print("🌤️  Récupération des données météo...")
    
    try:
        # Paramètres pour l'API OpenWeatherMap
        params = {
            'q': f"{Config.CITY},{Config.COUNTRY}",
            'appid': Config.WEATHER_API_KEY,
            'units': 'metric',  # Unités métriques (°C)
            'lang': 'fr'       # Langue française
        }
        
        print(f" Appel de l'API Météo pour {Config.CITY}...")
        response = requests.get(Config.WEATHER_URL, params=params)
        response.raise_for_status()
        
        print(" Données météo reçues avec succès!")
        data = response.json()
        
        # Extraction et formatage des données météo
        weather_description = data['weather'][0]['description'].capitalize()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        weather_news = {
            'title': f"Météo à {Config.CITY}",
            'description': weather_description,
            'temperature': f"Température: {temperature}°C",
            'humidity': f"Humidité: {humidity}%",
            'wind': f"Vent: {wind_speed} m/s"
        }
        
        return [weather_news]  # Retourne une liste pour uniformité
        
    except Exception as e:
        print(f" Erreur météo: {e}")
        return [{
            'title': 'Météo indisponible',
            'description': 'Impossible de récupérer les données météo'
        }]