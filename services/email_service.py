import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from config.config import Config

def create_email_content(news_items):
    """
    Crée le contenu HTML de l'email avec les news formatées
    """
    # En-tête avec date
    html_content = f"""
    <html>
    <head>
        <style>
            body {{ 
                font-family: Arial, sans-serif; 
                margin: 20px;
                background-color: #f5f5f5;
            }}
            .header {{ 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 30px;
                text-align: center;
                border-radius: 10px;
                margin-bottom: 20px;
            }}
            .news-container {{
                max-width: 600px;
                margin: 0 auto;
            }}
            .news-item {{ 
                background: white;
                border-left: 4px solid #667eea;
                margin: 15px 0;
                padding: 20px;
                border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }}
            .weather {{ border-left-color: #4CAF50; }}
            .news {{ border-left-color: #FF9800; }}
            .crypto {{ border-left-color: #9C27B0; }}
            h1 {{ margin: 0; font-size: 24px; }}
            h2 {{ color: #333; border-bottom: 2px solid #eee; padding-bottom: 10px; }}
            h3 {{ color: #444; margin-top: 0; }}
            p {{ color: #666; line-height: 1.6; }}
            .source {{ font-size: 12px; color: #888; font-style: italic; }}
            .footer {{
                text-align: center;
                margin-top: 30px;
                padding: 20px;
                color: #888;
                font-size: 12px;
            }}
        </style>
    </head>
    <body>
        <div class="news-container">
            <div class="header">
                <h1>📰 Votre Résumé Quotidien</h1>
                <p>Date: {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>
            </div>
    """
    
    # Organisation des news par catégorie
    categories = {
        'weather': {'title': '🌤️ Météo', 'items': [], 'class': 'weather'},
        'news': {'title': '📰 Actualités', 'items': [], 'class': 'news'}, 
        'crypto': {'title': '💰 Crypto-monnaies', 'items': [], 'class': 'crypto'}
    }
    
    # Répartition des news dans les catégories
    for i, item in enumerate(news_items):
        if i == 0:  # Première = météo
            categories['weather']['items'].append(item)
        elif i in [1, 2]:  # 2ème et 3ème = actualités
            categories['news']['items'].append(item)
        else:  # 4ème et 5ème = crypto
            categories['crypto']['items'].append(item)
    
    # Génération du contenu pour chaque catégorie
    for category, data in categories.items():
        if data['items']:
            html_content += f"<h2>{data['title']}</h2>"
            for item in data['items']:
                html_content += f"""
                <div class="news-item {data['class']}">
                    <h3>{item.get('title', 'Sans titre')}</h3>
                    <p>{item.get('description', 'Pas de description')}</p>
                    {f"<p><small>{item.get('temperature', '')}</small></p>" if item.get('temperature') else ''}
                    {f"<p><small>{item.get('humidity', '')}</small></p>" if item.get('humidity') else ''}
                    {f"<p><small>{item.get('wind', '')}</small></p>" if item.get('wind') else ''}
                    {f"<p class='source'>{item.get('source', '')}</p>" if item.get('source') else ''}
                    {f"<p><small>{item.get('market_cap', '')}</small></p>" if item.get('market_cap') else ''}
                </div>
                """
    
    # Pied de page
    html_content += """
            <div class="footer">
                <p> Email généré automatiquement - Bonne journée !</p>
                <p><small>Vous recevez cet email car vous êtes abonné au résumé quotidien.</small></p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return html_content

def send_email(news_items):
    """
    Envoie l'email avec le résumé des news
    """
    try:
        print(" Préparation de l'email...")
        
        # Création du message email
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f" Votre Résumé Quotidien - {datetime.now().strftime('%d/%m/%Y')}"
        msg['From'] = Config.EMAIL_SENDER
        msg['To'] = Config.EMAIL_RECEIVER
        
        # Création du contenu HTML
        html_content = create_email_content(news_items)
        
        # Attachement du contenu HTML
        msg.attach(MIMEText(html_content, 'html'))
        
        # Envoi de l'email via SMTP
        print(" Envoi de l'email en cours...")
        with smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT) as server:
            server.starttls()  # Chiffrement
            server.login(Config.EMAIL_SENDER, Config.EMAIL_PASSWORD)
            server.send_message(msg)
        
        print(" Email envoyé avec succès!")
        return True
        
    except Exception as e:
        print(f" Erreur lors de l'envoi de l'email: {e}")
        return False