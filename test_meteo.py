# test_meteo.py
from services.weather_service import get_weather_news

print("🧪 Test du Service Météo")
print("=" * 50)

def test_meteo():
    try:
        print("🌤️  Lancement du test météo...")
        print("📡 Connexion à l'API OpenWeatherMap...")
        
        # Appel du service météo
        resultats = get_weather_news()
        
        print("\n✅ Test réussi ! Données reçues :")
        print("=" * 40)
        
        if resultats:
            meteo = resultats[0]  # Premier élément de la liste
            
            print(f"📍 {meteo['title']}")
            print(f"📝 {meteo['description']}")
            print(f"🌡️  {meteo.get('temperature', 'Non disponible')}")
            print(f"💧 {meteo.get('humidity', 'Non disponible')}")
            print(f"💨 {meteo.get('wind', 'Non disponible')}")
            
            # Vérification des données
            print("\n🔍 Vérification des données :")
            print(f"   Type de données: {type(resultats)}")
            print(f"   Nombre d'éléments: {len(resultats)}")
            print(f"   Clés disponibles: {list(meteo.keys())}")
            
        else:
            print("❌ Aucune donnée météo reçue")
            
    except Exception as e:
        print(f"💥 Erreur lors du test: {e}")
        print("\n🔧 Dépannage :")
        print("   1. Vérifiez votre clé OpenWeatherMap dans .env")
        print("   2. Vérifiez votre connexion internet")
        print("   3. Vérifiez que la ville est correcte")

if __name__ == "__main__":
    test_meteo()