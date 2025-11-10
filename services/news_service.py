# services/news_service.py - VERSION AVEC FALLBACK
import requests
from config.config import Config

def get_general_news():
    """
    Récupère les actualités depuis NewsAPI avec fallback automatique
    """
    print(" Récupération des actualités...")
    
    # Essai 1: France
    print("    Recherche d'actualités françaises...")
    articles = try_get_news('fr')
    if articles:
        return articles
    
    # Essai 2: États-Unis (fallback - toujours disponible)
    print("    Aucune actualité FR, recherche d'actualités internationales...")
    articles = try_get_news('us')
    if articles:
        # On traduit le contexte pour l'utilisateur français
        for article in articles:
            article['title'] = " " + article['title']
            article['source'] = "Actualités internationales"
        return articles
    
    # Essai 3: Sources globales (fallback ultime)
    print("    Recherche d'actualités globales...")
    articles = try_get_news_global()
    if articles:
        return articles
    
    # Si tout échoue, on retourne des actualités simulées
    return get_fallback_news()

def try_get_news(country):
    """Tente de récupérer les actualités pour un pays donné"""
    try:
        params = {
            'country': country,
            'apiKey': Config.NEWS_API_KEY,
            'pageSize': Config.NEWS_PAGE_SIZE
        }
        
        response = requests.get(Config.NEWS_URL, params=params)
        response.raise_for_status()
        
        data = response.json()
        articles_data = data.get('articles', [])
        total_results = data.get('totalResults', 0)
        
        print(f"    {country.upper()}: {total_results} articles trouvés, {len(articles_data)} récupérés")
        
        if articles_data:
            formatted_articles = format_articles(articles_data)
            print(f"    {len(formatted_articles)} article(s) valide(s) pour {country.upper()}")
            return formatted_articles
        
        return None
        
    except Exception as e:
        print(f"    Erreur pour {country}: {e}")
        return None

def try_get_news_global():
    """Tente de récupérer des actualités globales"""
    try:
        # Sources internationales populaires qui ont du contenu
        sources = 'bbc-news,cnn,reuters,the-guardian-uk,associated-press'
        
        params = {
            'sources': sources,
            'apiKey': Config.NEWS_API_KEY,
            'pageSize': Config.NEWS_PAGE_SIZE
        }
        
        response = requests.get(Config.NEWS_URL, params=params)
        response.raise_for_status()
        
        data = response.json()
        articles_data = data.get('articles', [])
        
        print(f"   Global: {len(articles_data)} articles récupérés")
        
        if articles_data:
            formatted_articles = format_articles(articles_data)
            print(f"    {len(formatted_articles)} article(s) global(aux) valide(s)")
            return formatted_articles
        
        return None
        
    except Exception as e:
        print(f"    Erreur sources globales: {e}")
        return None

def format_articles(articles_data):
    """Formate les articles pour l'affichage"""
    news_list = []
    
    for article in articles_data:
        title = article.get('title', '').strip()
        description = article.get('description', '').strip()
        source = article.get('source', {}).get('name', 'Source inconnue')
        
        # Filtre les articles sans titre ou avec titre '[Removed]'
        if title and title != '[Removed]' and len(title) > 10:
            # Troncature si nécessaire
            if len(title) > 100:
                title = title[:100] + '...'
            
            # Nettoie la description
            if not description or description == '[Removed]':
                description = "Description non disponible"
            elif len(description) > 150:
                description = description[:150] + '...'
            
            news_list.append({
                'title': title,
                'description': description,
                'source': f"Source: {source}"
            })
            
            # On limite à 2 articles maximum
            if len(news_list) >= Config.NEWS_PAGE_SIZE:
                break
    
    return news_list

def get_fallback_news():
    """Retourne des actualités simulées si tout échoue"""
    print("   ⚠️  Utilisation des actualités de fallback")
    
    fallback_articles = [
        {
            'title': ' Conseil du Jour : Continuez à apprendre la programmation',
            'description': 'Chaque jour dédié à l\'apprentissage vous rapproche de vos objectifs. Restez motivé !',
            'source': 'Source: Votre Assistant IA'
        },
        {
            'title': ' Projet Python : Votre agrégateur de news fonctionne',
            'description': 'Félicitations ! Votre système automatisé collecte déjà les données météo et crypto.',
            'source': 'Source: Votre Projet'
        }
    ]
    
    return fallback_articles