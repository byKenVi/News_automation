# main.py - VERSION SIMPLIFIÉE ET CORRECTE
import time
import sys
from datetime import datetime

# Import des services
from services.weather_service import get_weather_news
from services.news_service import get_general_news
from services.crypto_service import get_crypto_news
from services.email_service import send_email
from config.config import Config

def collect_and_send_news():
    """
    Fonction principale qui collecte toutes les news et envoie l'email
    """
    print(f" Collecte des news démarrée à {datetime.now()}")
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
        print(f"    Crypto: {len(crypto_news)}")
        
        # Envoi de l'email
        if all_news:
            print("\n Envoi de l'email...")
            success = send_email(all_news)
            if success:
                print(" Email envoyé avec succès!")
                return True
            else:
                print(" Échec de l'envoi de l'email")
                return False
        else:
            print(" Aucune news à envoyer")
            return False
            
    except Exception as e:
        print(f" Erreur générale: {e}")
        return False

def main():
    """
    Fonction principale - TOUJOURS exécute une fois
    """
    print(" Démarrage de l'agrégateur de news...")
    
    # Exécution immédiate
    success = collect_and_send_news()
    
    if success:
        print("\n Script terminé avec succès!")
    else:
        print("\ Script terminé avec des erreurs")
    
    # Attendre un peu avant de fermer
    print("Fermeture dans 5 secondes...")
    time.sleep(5)

if __name__ == "__main__":
    main()