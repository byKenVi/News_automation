# test_news.py
from services.news_service import get_general_news

print("🧪 Test du Service Actualités")
print("=" * 50)

def test_actualites():
    try:
        print(" Lancement du test actualités...")
        print(" Connexion à l'API NewsAPI...")
        
        # Appel du service actualités
        articles = get_general_news()
        
        print(f"\n Test réussi ! {len(articles)} article(s) récupéré(s)")
        print("=" * 40)
        
        if articles:
            for i, article in enumerate(articles, 1):
                print(f"\n Article {i}:")
                print(f"    Titre: {article['title']}")
                print(f"    Description: {article['description']}")
                print(f"    {article.get('source', 'Source non spécifiée')}")
                
                # Vérification de la longueur
                if len(article['title']) > 80:
                    print("   ⚠️  Titre tronqué (trop long)")
            
            # Statistiques
            print(f"\n Statistiques :")
            print(f"   Total articles: {len(articles)}")
            print(f"   Type de données: {type(articles)}")
            print(f"   Structure d'un article: {list(articles[0].keys())}")
            
        else:
            print("❌ Aucun article récupéré")
            
    except Exception as e:
        print(f" Erreur lors du test: {e}")
        print("\n Dépannage :")
        print("   1. Vérifiez votre clé NewsAPI dans .env")
        print("   2. Vérifiez votre connexion internet")
        print("   3. Vérifiez que le pays (NEWS_COUNTRY) est correct")

if __name__ == "__main__":
    test_actualites()