# services/news_service.py - VERSION AVEC PLUS DE DÉTAILS
import requests
from datetime import datetime
from config.config import Config

def get_general_news():
    """
    Récupère les TOP articles avec détails complets
    """
    print(" Récupération des TOP actualités avec détails...")
    
    articles = get_top_articles()
    
    if articles:
        articles_fr = enrich_articles_with_details(articles)
        print(f" {len(articles_fr)} article(s) détaillé(s) en français")
        return articles_fr
    
    return get_educational_fallback()

def get_top_articles():
    """
    Récupère les articles avec tous les détails disponibles
    """
    try:
        # Sujets populaires pour développeurs
        popular_queries = [
            'technology', 'artificial intelligence', 'programming',
            'science', 'innovation', 'cybersecurity'
        ]
        
        all_articles = []
        
        for query in popular_queries:
            print(f"    Recherche détaillée: {query}")
            articles = search_detailed_articles(query)
            if articles:
                all_articles.extend(articles)
            
            if len(all_articles) >= 8:  # Plus d'articles pour mieux filtrer
                break
        
        # Filtrage qualité amélioré
        quality_articles = []
        for article in all_articles:
            if is_high_quality_article(article):
                quality_articles.append(article)
        
        print(f"    {len(quality_articles)} article(s) de haute qualité")
        return quality_articles[:Config.NEWS_PAGE_SIZE]
        
    except Exception as e:
        print(f" Erreur recherche articles détaillés: {e}")
        return None

def search_detailed_articles(query):
    """
    Recherche avec récupération de tous les détails
    """
    try:
        params = {
            'q': query,
            'sortBy': 'popularity',
            'language': 'fr',
            'apiKey': Config.NEWS_API_KEY,
            'pageSize': 4,  
            'searchIn': 'title,description'  # Recherche dans titre ET description
        }
        
        response = requests.get('https://newsapi.org/v2/everything', params=params)
        response.raise_for_status()
        
        data = response.json()
        return data.get('articles', [])
        
    except Exception as e:
        print(f"    Erreur recherche détaillée '{query}': {e}")
        return []

def is_high_quality_article(article):
    """
    Vérifie si l'article a suffisamment de détails pour être intéressant
    """
    title = article.get('title', '').strip()
    description = article.get('description', '').strip()
    content = article.get('content', '').strip()
    author = article.get('author', '')
    
    # Filtres qualité
    has_good_title = title and title != '[Removed]' and len(title) > 15
    has_good_description = description and description != '[Removed]' and len(description) > 40
    has_content = content and content != '[Removed]' and len(content) > 100
    has_author = author and len(author) > 3
    
    return has_good_title and has_good_description and (has_content or has_author)

def enrich_articles_with_details(articles):
    """
    Enrichit les articles avec tous les détails disponibles
    """
    enriched_articles = []
    
    for article in articles:
        # Extraction de tous les détails
        original_title = article.get('title', '')
        original_description = article.get('description', '')
        author = article.get('author', 'Auteur inconnu')
        source = article.get('source', {}).get('name', 'Source internationale')
        url = article.get('url', '#')
        published_at = article.get('publishedAt', '')
        content_preview = article.get('content', '')[:200] + '...' if article.get('content') else ''
        
        # Traduction/adaptation française
        french_title = translate_to_french(original_title)
        french_description = translate_to_french(original_description)
        
        # Formatage date
        formatted_date = format_date(published_at) if published_at else 'Date non disponible'
        
        # Emoji contextuel
        emoji = get_context_emoji(original_title.lower())
        french_title = f"{emoji} {french_title}"
        
        # Construction description enrichie
        enriched_description = build_enriched_description(
            french_description, author, formatted_date, content_preview
        )
        
        enriched_articles.append({
            'title': french_title,
            'description': enriched_description,
            'source': f" {source}",
            'author': f" {author}" if author and author != 'Auteur inconnu' else '',
            'date': f" {formatted_date}",
            'url': url,
            'content_preview': content_preview,
            'reading_time': estimate_reading_time(content_preview)
        })
    
    return enriched_articles

def translate_to_french(text):
    """
    Traduction simple vers le français
    """
    if not text:
        return "Description non disponible"
    
    translation_map = {
        'AI': 'Intelligence Artificielle',
        'artificial intelligence': 'intelligence artificielle',
        'machine learning': 'apprentissage automatique',
        'programming': 'programmation',
        'developer': 'développeur',
        'code': 'code',
        'software': 'logiciel',
        'technology': 'technologie',
        'innovation': 'innovation',
        'breakthrough': 'avancée majeure',
        'study': 'étude',
        'research': 'recherche',
        'scientists': 'scientifiques',
        'discovery': 'découverte',
        'develop': 'développent',
        'create': 'créent',
        'find': 'découvrent',
        'new': 'nouvelle',
        'announces': 'annonce'
    }
    
    translated = text
    for eng, fr in translation_map.items():
        translated = translated.replace(eng, fr)
        translated = translated.replace(eng.lower(), fr.lower())
        translated = translated.replace(eng.title(), fr)
    
    return translated

def format_date(date_string):
    """
    Formate la date en français
    """
    try:
        # Conversion de "2024-01-15T08:00:00Z" en datetime
        date_obj = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
        return date_obj.strftime('%d/%m/%Y à %H:%M')
    except:
        return date_string

def estimate_reading_time(text):
    """
    Estime le temps de lecture (environ 200 mots/minute)
    """
    if not text:
        return "Temps de lecture non disponible"
    
    word_count = len(text.split())
    minutes = max(1, round(word_count / 200))
    
    return f" {minutes} min de lecture"

def build_enriched_description(description, author, date, content_preview):
    """
    Construit une description enrichie avec tous les détails
    """
    parts = []
    
    # Description principale
    if description:
        parts.append(description)
    
    # Auteur si disponible
    if author and author != 'Auteur inconnu':
        parts.append(f"Par {author}")
    
    # Date de publication
    if date:
        parts.append(f"Publié {date}")
    
    # Extrait du contenu si disponible
    if content_preview and len(content_preview) > 50:
        parts.append(f"Extrait: {content_preview}")
    
    return " | ".join(parts)

def get_context_emoji(title):
    """
    Retourne un emoji basé sur le contexte
    """
    tech_keywords = ['ai', 'artificial intelligence', 'tech', 'robot', 'programming', 'code', 'software']
    science_keywords = ['science', 'research', 'discovery', 'study', 'scientists']
    climate_keywords = ['climate', 'environment', 'planet', 'earth']
    health_keywords = ['health', 'medical', 'medicine', 'disease']
    
    if any(word in title for word in tech_keywords):
        return '🤖'
    elif any(word in title for word in science_keywords):
        return '🔬'
    elif any(word in title for word in climate_keywords):
        return '🌍'
    elif any(word in title for word in health_keywords):
        return '🏥'
    else:
        return '📰'

def get_educational_fallback():
    """
    Fallback avec détails enrichis
    """
    print("    Utilisation des actualités éducatives enrichies")
    
    return [
        {
            'title': ' Votre Projet Python : Agrégateur de News Opérationnel',
            'description': f"Félicitations ! Votre système collecte données météo, crypto et actualités | ✍️ Votre Assistant IA | 📅 {datetime.now().strftime('%d/%m/%Y')} | ⏱️ 1 min de lecture",
            'source': ' Votre Réussite',
            'author': ' Votre Assistant IA',
            'date': f" {datetime.now().strftime('%d/%m/%Y')}",
            'reading_time': '⏱️ 1 min de lecture'
        }
    ]