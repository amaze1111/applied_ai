import google.generativeai as genai
from config import GEMINI_API_KEY

def summarizer(news_results):
    gemini_api_key = GEMINI_API_KEY
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')

    news_text = "\n".join([
        f"Title: {result.get('title', '')}\n"
        f"Source: {result.get('source', '')}\n"
        f"Date: {result.get('date', '')}\n"
        f"Snippet: {result.get('snippet', '')}\n"
        for result in news_results[:10]
    ])

    prompt = f"Provide a concise summary of these news articles, highlighting the key points and main developments.:\n{news_text}\n\nSummary:"    
    
    response = model.generate_content(prompt)
    
    return response.text