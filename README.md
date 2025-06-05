# Project: Modular News Summarizer with Telegram Delivery

This project fetches India-specific news, summarizes the top 3 stories using Gemini AI, and sends the summaries to a Telegram chat daily at 7AM IST.

## Structure
- `config.py`: Loads environment variables and API keys.
- `news_fetcher.py`: Fetches news articles using SerpAPI.
- `summarizer.py`: Summarizes news using Gemini AI.
- `telegram_sender.py`: Sends messages to Telegram using the official API.
- `main.py`: Main entry point to run the workflow.

## Setup

1. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
2. Run the workflow manually:
   ```powershell
   python main.py
   ```

## Scheduling (Optional)
To schedule the script to run daily at 7AM IST, use Windows Task Scheduler or a cloud scheduler to run `python main.py` at the desired time.

## Requirements
- Python 3.8+
- Packages: `requests`, `python-dotenv`, `google-generativeai`

## License
MIT



## Step-by-Step flow and Instructions
Use python for code generation
For messgaing - Telegram is used because it's api is free. For whatsapp, there is a third party service called callmebot but official access is paid.
For news scraping and summary - Gemini and SerpApi is used

For telegram bot id - 
- Go to telegram app on the phone
- type @botfather to find an account
- choose instructions to create a bot : /newbot
- give a name
- go to the bot: t.me/<name_of_the_bot>
- store the token somewhere as it will be required later. This is the bot id used in this program.
- press start and send a message

For Telegram chat id - 
- In the url https://api.telegram.org/<your_key>/getUpdates, replace "your_key" with token stored in previous step
- Append bot as suffix. For eg: if token or your_key is "abc", new URL will be https://api.telegram.org/botabc/getUpdates
- go to the new URL and find chat id from the json generated on that url


## After adding FastAPi code ##
- Run, uvicorn api:app --reload
- Follow the generated url


## Fast API to Public URL ##
- In one terminal, uvicorn api:app --host 0.0.0.0 --port 8000
- Download ngrok from https://ngrok.com/download
- Extract and save the new folder as Path in environment variable
- Authenticate ngrok
- In another terminal, ngrok http 8000
- A new URL will be generated like https://41ca-106-51-164-224.ngrok-free.app
- Simply, run https://41ca-106-51-164-224.ngrok-free.app/summarize_and_send?topic=YourTopic by changing YourTopic. Telegram message will also be sent.

## Creating frontend using Next.js, Shadcn for ui components
- Run this in the terminal: npx create-next-app -e with-supabase news-frontend ##Here "news" is the project name.## 
- Run this in the terminal: cd news-frontend
- Run this in the terminal: npm run dev