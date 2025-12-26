import os
import requests
import random

PIXABAY_API_KEY = os.environ.get("PIXABAY_API_KEY")

KEYWORDS = [
    "nature",
    "forest",
    "mountain",
    "river",
    "sunset",
    "sunrise",
    "beach",
    "sky"
]

def get_video():
    keyword = random.choice(KEYWORDS)

    url = "https://pixabay.com/api/videos/"
    params = {
        "key": PIXABAY_API_KEY,
        "q": keyword,
        "per_page": 30,
        "safesearch": "true"
    }

    r = requests.get(url, params=params, timeout=20)
    data = r.json()

    if "hits" not in data or len(data["hits"]) == 0:
        return None

    video = random.choice(data["hits"])
    video_url = video["videos"]["small"]["url"]

    return video_url, keyword
