from user_input import get_user_input
from news_fetcher import fetch_news
from summarizer import summarizer
from telegram_sender import send_telegram_message

def main():
    # topic = get_user_input()  
    # Skip user input for scheduler
    topic = "Bengaluru"
    news_results = fetch_news(topic)
    summary = summarizer(news_results)
    send_telegram_message(summary)

# def scheduled_job():
#     news = fetch_news()
#     summary = summarizer(news)
#     send_telegram_message(summary)


if __name__ == "__main__":
    main()