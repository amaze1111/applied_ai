from news_fetcher import fetch_news
from telegram_sender import send_telegram_message

def main():
    news_results = fetch_news()
    send_telegram_message(news_results)

if __name__ == "__main__":
    main()
