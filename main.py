import schedule
import time
from datetime import datetime

# Import des services
from services.weather_service import get_weather_news
from services.news_service import get_general_news
from services.crypto_service import get_crypto_news
from services.email_service import send_email

# Import de la configuration - AJOUT IMPORTANT !
from config.config import Config

def collect_and_send_news():
    """
    Fonction principale qui collecte toutes les news et envoie l'email
    """
    print(f"\n Collecte des news démarrée à {datetime.now()}")
    print("=" * 50)
    
    try:
        # Collecte des données
        print(" Collecte des données en cours...")
        weather_news = get_weather_news()
        general_news = get_general_news()
        crypto_news = get_crypto_news()
        
        # Combinaison de toutes les news
        all_news = weather_news + general_news + crypto_news
        
        print(f"\n Récapitulatif : {len(all_news)} news collectées")
        print(f"     Météo: {len(weather_news)}")
        print(f"    Actualités: {len(general_news)}")
        print(f"   ₿ Crypto: {len(crypto_news)}")
        
        # Envoi de l'email
        if all_news:
            success = send_email(all_news)
            if success:
                print(" Tâche terminée avec succès!")
            else:
                print(" Échec de l'envoi de l'email")
        else:
            print(" Aucune news à envoyer")
            
    except Exception as e:
        print(f" Erreur générale: {e}")

def main():
    """
    Fonction principale avec planification
    """
    print(" Démarrage de l'agrégateur de news...")
    print(f" Envoi programmé tous les jours à {Config.SCHEDULE_TIME}")
    
    # Planification de l'exécution quotidienne
    schedule.every().day.at(Config.SCHEDULE_TIME).do(collect_and_send_news)
    
    # Exécution immédiate pour test
    print("\n🧪 Test immédiat...")
    collect_and_send_news()
    
    print(f"\n📡 Service en écoute...")
    print("Pour arrêter: Ctrl + C")
    
    # Boucle principale
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)
    except KeyboardInterrupt:
        print("\n👋 Arrêt du service...")

if __name__ == "__main__":
    main()