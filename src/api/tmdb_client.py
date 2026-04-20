# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

def get_movies():
    url = f"{BASE_URL}/movie/popular"
    params = {
        "api_key": API_KEY,
        "language": "tr-TR",
        "page": 1
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def main():
    data = get_movies()
    movies = data["results"]

    cleaned = []
    for m in movies:
        cleaned.append({
            "title": m["title"],
            "overview": m["overview"],
            "poster": f"https://image.tmdb.org/t/p/w500{m['poster_path']}"
        })

    with open("data/movies.json", "w", encoding="utf-8") as f:
        json.dump(cleaned, f, ensure_ascii=False, indent=2)

    print("Filmler kaydedildi!")

if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
