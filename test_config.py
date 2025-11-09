from config.config import Config

print("🧪 Test de la configuration...")

# Test des variables de base
print(f"📍 Ville configurée: {Config.CITY}")
print(f"🌍 Pays configuré: {Config.COUNTRY}")
print(f"📧 Expéditeur: {Config.EMAIL_SENDER}")
print(f"⏰ Heure d'envoi: {Config.SCHEDULE_TIME}")

# Test des configurations crypto
print(f"₿ Cryptos suivies: {Config.CRYPTO_IDS}")
print(f"💰 Devise crypto: {Config.CRYPTO_CURRENCY}")

print("✅ Test de configuration terminé!")