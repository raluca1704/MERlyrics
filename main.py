import requests

API_KEY = "TOKENUL_TĂU_GENIUS"
BASE_URL = "https://api.genius.com"


def search_song(song_title, artist_name):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    search_url = f"{BASE_URL}/search"
    params = {"q": f"{song_title} {artist_name}"}

    response = requests.get(search_url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["response"]["hits"]:
            return data["response"]["hits"][0]["result"]["url"]
    return None


song_url = search_song("Someone Like You", "Adele")
print(song_url)
