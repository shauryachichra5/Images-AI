import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dotenv import load_dotenv
import requests

load_dotenv(override=True)
URL=os.getenv("UNSPLASH_URL")
ACCESS_KEY=os.getenv("UNSPLASH_ACCESS_KEY")

def search_unsplash(query, per_page=5):
    url = URL
    headers = {"Accept-Version": "v1"}
    params = {
        "query": query,
        "per_page": per_page,
        "client_id": ACCESS_KEY
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data['results']
        for i, result in enumerate(data["results"], start=1):
            print(f"{i}. {result['urls']['regular']} (by {result['user']['name']})")
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None
