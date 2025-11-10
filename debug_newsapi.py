# debug_newsapi.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def debug_newsapi():
    print("🔧 Debug NewsAPI")
    print("=" * 40)
    
    # Configuration
    NEWS_API_KEY = os.getenv('NEWS_API_KEY')
    NEWS_URL = "https://newsapi.org/v2/top-headlines"
    
    print(f"🔑 Clé API: {NEWS_API_KEY[:10]}...{NEWS_API_KEY[-5:] if NEWS_API_KEY else 'NON TROUVÉE'}")
    
    # Test 1: France
    print("\n1. 🇫🇷 Test avec pays=fr")
    params_fr = {
        'country': 'fr',
        'apiKey': NEWS_API_KEY,
        'pageSize': 5
    }
    
    try:
        response = requests.get(NEWS_URL, params=params_fr)
        print(f"   Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"   Total articles: {data.get('totalResults', 0)}")
            print(f"   Articles reçus: {len(data.get('articles', []))}")
            
            if data.get('articles'):
                for i, article in enumerate(data['articles'][:3]):
                    print(f"   {i+1}. {article.get('title', 'Sans titre')[:60]}...")
            else:
                print("   ❌ Aucun article trouvé pour la France")
        else:
            print(f"   ❌ Erreur API: {response.status_code}")
            print(f"   Message: {response.text}")
            
    except Exception as e:
        print(f"   💥 Exception: {e}")
    
    # Test 2: États-Unis (pour comparer)
    print("\n2. 🇺🇸 Test avec pays=us")
    params_us = {
        'country': 'us', 
        'apiKey': NEWS_API_KEY,
        'pageSize': 5
    }
    
    try:
        response = requests.get(NEWS_URL, params=params_us)
        print(f"   Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"   Total articles: {data.get('totalResults', 0)}")
            print(f"   Articles reçus: {len(data.get('articles', []))}")
        else:
            print(f"   ❌ Erreur API: {response.status_code}")
            
    except Exception as e:
        print(f"   💥 Exception: {e}")
    
    # Test 3: Sans pays (sources globales)
    print("\n3. 🌍 Test sans pays (sources globales)")
    params_global = {
        'sources': 'bbc-news,cnn,reuters',
        'apiKey': NEWS_API_KEY, 
        'pageSize': 5
    }
    
    try:
        response = requests.get(NEWS_URL, params=params_global)
        print(f"   Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"   Articles reçus: {len(data.get('articles', []))}")
        else:
            print(f"   ❌ Erreur API: {response.status_code}")
            
    except Exception as e:
        print(f"   💥 Exception: {e}")

if __name__ == "__main__":
    debug_newsapi()