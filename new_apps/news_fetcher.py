from config import SERPAPI_KEY, GEMINI_API_KEY
# from textwrap import dedent
from agno.agent import Agent
from agno.tools.serpapi import SerpApiTools
from agno.models.google import Gemini

def fetch_news():
    query="India"
    num_results=10

    serp_api_key = SERPAPI_KEY
    gemini_api_key = GEMINI_API_KEY

    if serp_api_key and gemini_api_key:
        researcher = Agent(
            name="Researcher",
            role="Searches for news articles related to the query and summarizes them.",
            model=Gemini(id="gemini-2.0-flash", api_key=gemini_api_key),
            description=[
                f"You are a world-class news expert.",
                f"You are an expert in finding the latest news articles.",
                f"You will parse the results from the SERPAPI and summarize them."
            ],
            instructions=[
                f"For a given query, search for the latest news articles related to that query.",
                f"Create a list of top {num_results}, with a title and a short description.",
                f"Make sure to include the source of the news article.",
                f"Make sure the results are relevant to the query.",
                f"Make sure the results are from the last 24 hours.",
                f"Make sure the results are from India.",
                f"Make sure the results are from reliable sources.",
                f"Make sure the results are not biased.",
                f"Make sure the results are not fake news.",
                f"Make sure the results are not clickbait.",
                f"Make sure the results are not misleading.",
                f"Make sure the results are not opinion pieces.",
                f"Make sure the results are not sponsored.",
                f"Make sure the results are not ads.",
                f"Make sure the length of the short description is not more than 10 words.",
                f"Remember: the quality of the results is important.",
            ],
            tools=[SerpApiTools(api_key=serp_api_key)],
            add_datetime_to_instructions=True,
        )
        response = researcher.run(f"Research about {query} and create a list of top {num_results} results", stream=False)
        return response.content
    else:
        print("SERPAPI_KEY or GEMINI_API_KEY is missing or empty. Please check your .env or environment variables.")