import requests
from config import SERPAPI_KEY

BASE_URL = "https://serpapi.com/search"


def search_amazon(query):
    params = {
        "engine": "amazon",
        "amazon_domain": "amazon.eg",
        "api_key": SERPAPI_KEY,
        "k": query
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        raise Exception(f"SerpApi Error: {response.text}")

    return response.json()
