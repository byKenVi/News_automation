import requests
from config.config import Config

# 2. FONCTION PRINCIPALE
def get_crypto_news():
    """
    Récupère les informations des cryptomonnaies depuis CoinGecko
    Retourne une liste de dictionnaires avec les données formatées
    """
    print("Récupération des données crypto...")
    
    try:
        # 3. PRÉPARATION DE LA REQUÊTE
        params = {
            'vs_currency': Config.CRYPTO_CURRENCY,  # 'eur' ou 'usd'
            'ids': Config.CRYPTO_IDS,               # 'bitcoin,ethereum,solana'
            'order': 'market_cap_desc',             # Tri par capitalisation
            'per_page': Config.CRYPTO_LIMIT,        # Nombre de résultats
            'page': 1,                              # Première page
            'sparkline': False,                     # Pas de graphique sparkline
            'price_change_percentage': '24h'        # Variation sur 24h
        }
        
        print(f"📡 Appel de l'API CoinGecko...")
        print(f"   Cryptos: {Config.CRYPTO_IDS}")
        print(f"   Devise: {Config.CRYPTO_CURRENCY}")
                # 4. APPEL À L'API
        """
        requests.get() envoie une requête HTTP GET
        C'est comme taper une URL dans un navigateur, mais en code
        """
        response = requests.get(Config.CRYPTO_URL, params=params)
        
        # 5. VÉRIFICATION DE LA RÉPONSE
        """
        response.raise_for_status() vérifie si la requête a réussi
        Si statut HTTP ≠ 200 (OK), il lève une exception
        """
        response.raise_for_status()
        
        print(f"✅ API contactée avec succès!")        # 6. TRAITEMENT DES DONNÉES
        """
        response.json() convertit la réponse JSON en dictionnaire Python
        """
        cryptos_data = response.json()
        
        print(f"📊 Données reçues pour {len(cryptos_data)} cryptomonnaie(s)")
        
        # 7. FORMATAGE DES RÉSULTATS
        crypto_news = []
        
        for crypto in cryptos_data:
            """
            Chaque 'crypto' est un dictionnaire avec pleins de données
            On extrait seulement ce qui nous intéresse
            """
            
            # Extraction des données de base
            name = crypto.get('name', 'Inconnu')
            symbol = crypto.get('symbol', '').upper()  # BTC, ETH, etc.
            current_price = crypto.get('current_price', 0)
            price_change = crypto.get('price_change_percentage_24h', 0)
            market_cap = crypto.get('market_cap', 0)
            
            # 8. LOGIQUE MÉTIER : déterminer la tendance
            """
            Si price_change > 0 → marché haussier (📈)
            Si price_change < 0 → marché baissier (📉)
            """
            trend = "📈" if price_change > 0 else "📉"
            
            # 9. FORMATAGE DES CHAÎNES
            """
            On formate les nombres pour une belle présentation :
            - :.2f → 2 décimales pour les prix
            - :+.2f → signe + pour les variations positives
            - :, → séparateurs de milliers
            """
            formatted_price = f"{current_price:,.2f}€"
            formatted_change = f"{price_change:+.2f}%"
            formatted_market_cap = f"{market_cap:,.0f}€"
            
            # 10. CRÉATION DE L'OBJET NEWS
            crypto_news.append({
                'title': f"{name} ({symbol})",
                'description': f"Prix: {formatted_price} | Variation 24h: {formatted_change} {trend}",
                'market_cap': f"Market Cap: {formatted_market_cap}",
                'price_change': price_change  # Gardé pour traitement ultérieur
            })
            
            print(f"   ✅ {name} traité")        # 11. RETOUR DU RÉSULTAT
        return crypto_news
        
    except requests.exceptions.RequestException as e:
        # 12. GESTION D'ERREURS SPÉCIFIQUE API
        print(f"Erreur réseau: {e}")
        return [{
            'title': 'Erreur réseau crypto',
            'description': 'Impossible de contacter CoinGecko'
        }]
        
    except Exception as e:
        # 13. GESTION D'ERREURS GÉNÉRIQUE
        print(f"Erreur inattendue: {e}")
        return [{
            'title': 'Erreur crypto',
            'description': 'Problème lors du traitement des données'
        }]