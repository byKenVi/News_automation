import schedule
import time
from datetime import datetime
import os
import sys
import logging


logging.basicConfig(
    level=logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("news_automation.log"),
        logging.StreamHandler()
    ]
    )
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
    logging.info(" Démarrage de la collecte des news...")
    
    try:
      
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
                logging.info(" Tâche terminée avec succès!")
            else:
                logging.info(" Échec de l'envoi de l'email")
        else:
            logging.warning(" Aucune news à envoyer")
            
    except Exception as e:
        logging.error(f" Erreur générale: {e}")
        return False
    
def run_once_and_exit():

    print(f"Lancement unique à {datetime.now()}")
    sucess = collect_and_send_news()
    if sucess:
        print(" Tâche terminée avec succès!")
    else:
        print(" Échec de la tâche")

    sys.exit(0 if sucess else 1)

    def run_scheduled():
    
        print(f"Lancement programmé à {datetime.now()}")

        schedule.every().day.at(Config.SCHEDULE_TIME).do(collect_and_send_news)

        # Execution pour test
        print(" Exécution immédiate pour test...")
        collect_and_send_news()
        print(" Pour arrêter le script, utilisez Ctrl+C")

        try:
            while True:
                schedule.run_pending()
                time.sleep(60)
        except KeyboardInterrupt:
            print("Arret mannuel du script.")

    if __name__ == "__main__":
        if len(sys.argv) > 1 and sys.argv[1] == "--auto":
            run_once_and_exit()
        else:
            run_scheduled()
