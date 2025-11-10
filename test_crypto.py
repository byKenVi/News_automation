# test_crypto.py
from services.crypto_service import get_crypto_news

print(" Test du service crypto...")
print("=" * 50)

# Appel de la fonction
results = get_crypto_news()

print("\n RÉSULTATS OBTENUS :")
print("=" * 50)

for i, crypto in enumerate(results, 1):
    print(f"{i}. {crypto['title']}")
    print(f"    {crypto['description']}")
    print(f"    {crypto.get('market_cap', 'N/A')}")
    print()

print(f"🎯 Total: {len(results)} cryptomonnaie(s) récupérée(s)")