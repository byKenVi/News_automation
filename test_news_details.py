# test_news_details.py
from services.news_service import get_general_news

print("🧪 Test Articles avec Détails Complets")
print("=" * 50)

def test_news_details():
    print(" Recherche des articles avec tous les détails...")
    
    articles = get_general_news()
    
    print(f"\n {len(articles)} article(s) détaillé(s) récupéré(s)")
    print("=" * 50)
    
    for i, article in enumerate(articles, 1):
        print(f"\n ARTICLE {i}")
        print("-" * 30)
        print(f"  TITRE: {article['title']}")
        print(f" DESCRIPTION: {article['description']}")
        
        # Affichage des détails supplémentaires
        if article.get('author'):
            print(f"   {article['author']}")
        if article.get('date'):
            print(f"   {article['date']}")
        if article.get('source'):
            print(f"   {article['source']}")
        if article.get('reading_time'):
            print(f"   {article['reading_time']}")
        
        print(f"🔗 URL: {article.get('url', 'Non disponible')}")

if __name__ == "__main__":
    test_news_details()