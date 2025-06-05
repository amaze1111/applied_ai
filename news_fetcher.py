from config import SERPAPI_KEY
from serpapi import GoogleSearch

def fetch_news(query):

    serp_api_key = SERPAPI_KEY

    if serp_api_key:
        params = {
            "engine": "google",
            "q": f"{query} news",
            "tbm": "nws",
            "api_key": serp_api_key
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        return results.get("news_results", [])