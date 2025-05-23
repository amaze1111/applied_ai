import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_telegram_message(summary):
    bot_token=TELEGRAM_BOT_TOKEN
    chat_id=TELEGRAM_CHAT_ID
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': summary
    }
    requests.post(url, data=payload)