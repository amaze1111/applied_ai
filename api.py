from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from supabase import create_client, Client
import os
from dotenv import load_dotenv
from news_fetcher import fetch_news
from summarizer import summarizer
from telegram_sender import send_telegram_message
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

# Add this after creating the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your ngrok URL for more security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve the HTML form at the root URL
@app.get("/", response_class=HTMLResponse)
async def serve_form():
    with open("news_form.html", "r", encoding="utf-8") as f:
        return f.read()

class UserRequest(BaseModel):
    keyword: str
    phone_number: str

@app.post("/summarize_and_send")
def summarize_and_send(request: UserRequest):
    # Check if user already exists
    existing = supabase.table("news_users").select("topics_of_interest").eq("phone_number", request.phone_number).execute()
    if existing.data:
        # User exists, append topic if not already present
        topics = existing.data[0]["topics_of_interest"].split(",")
        if request.keyword not in topics:
            topics.append(request.keyword)
        topics_str = ",".join(topics)
    else:
        # New user
        topics_str = request.keyword

    data = {
        "topics_of_interest": topics_str,
        "phone_number": request.phone_number
    }
    supabase.table("news_users").upsert(data).execute()

    # Fetch news, summarize, and send Telegram message
    news_results = fetch_news(request.keyword)
    summary = summarizer(news_results)
    send_telegram_message(summary)

    return {
        "message": "User info stored and Telegram message sent",
        "data": data,
        "summary": summary
    }