# test_tous_services.py
from services.weather_service import get_weather_news
from services.news_service import get_general_news
from services.crypto_service import get_crypto_news

print("🧪 Test Complet - Tous les Services")
print("=" * 50)

def test_tous_services():
    print(" Lancement des tests pour les 3 services...\n")
    
    # Test Météo
    print("1. 🌤️  TEST MÉTÉO")
    print("-" * 30)
    try:
        meteo = get_weather_news()
        if meteo and len(meteo) > 0:
            print(f" Météo: {meteo[0]['title']}")
            print(f"   Description: {meteo[0]['description']}")
        else:
            print(" Échec météo")
    except Exception as e:
        print(f" Erreur météo: {e}")
    
    # Test Actualités
    print("\n2. 📰 TEST ACTUALITÉS")
    print("-" * 30)
    try:
        news = get_general_news()
        if news and len(news) > 0:
            print(f" Actualités: {len(news)} article(s)")
            for i, article in enumerate(news[:2], 1):  # Affiche max 2 articles
                print(f"   {i}. {article['title'][:60]}...")
        else:
            print(" Échec actualités")
    except Exception as e:
        print(f" Erreur actualités: {e}")
    
    # Test Crypto
    print("\n3. ₿ TEST CRYPTO")
    print("-" * 30)
    try:
        crypto = get_crypto_news()
        if crypto and len(crypto) > 0:
            print(f" Crypto: {len(crypto)} monnaie(s)")
            for i, monnaie in enumerate(crypto, 1):
                print(f"   {i}. {monnaie['title']}")
        else:
            print(" Échec crypto")
    except Exception as e:
        print(f" Erreur crypto: {e}")
    
    # Résumé final
    print("\n" + "=" * 50)
    print(" RÉSUMÉ DES TESTS")
    print("=" * 50)
    
    services = [
        ("Météo", meteo if 'meteo' in locals() else None),
        ("Actualités", news if 'news' in locals() else None),
        ("Crypto", crypto if 'crypto' in locals() else None)
    ]
    
    for nom, data in services:
        if data and len(data) > 0:
            print(f" {nom}: FONCTIONNEL ({len(data)} élément(s))")
        else:
            print(f" {nom}: ÉCHEC")

if __name__ == "__main__":
    test_tous_services()