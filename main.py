import requests
import json

# token genuis
API_KEY = "Xv8XYOrEq2OlSeBWOnwZJWjkokc9zDAFuntmF_Q74ph802EyL6_q3YUuHh1SyTit"
BASE_URL = "https://api.genius.com"


# Funcție pentru a căuta o melodie și a obține detalii
def search_song(song_title, artist_name):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    search_url = f"{BASE_URL}/search"
    params = {"q": f"{song_title} {artist_name}"}

    response = requests.get(search_url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["response"]["hits"]:
            song_data = data["response"]["hits"][0]["result"]
            return {
                "title": song_data["title"],
                "artist": song_data["primary_artist"]["name"],
                "url": song_data["url"]
            }
    return None


# Listă de melodii și artiști pentru testare
songs = [
    ("Someone Like You", "Adele"),
    ("Blinding Lights", "The Weeknd"),
    ("Shape of You", "Ed Sheeran"),
    ("Bohemian Rhapsody", "Queen"),
    ("Billie Jean", "Michael Jackson")
]

# Colectăm datele pentru fiecare melodie
song_data_list = []
for title, artist in songs:
    song_info = search_song(title, artist)
    if song_info:
        song_data_list.append(song_info)

# Salvăm datele într-un fișier JSON
with open("songs_data.json", "w", encoding="utf-8") as json_file:
    json.dump(song_data_list, json_file, indent=4, ensure_ascii=False)

print("Datele au fost salvate în songs_data.json")
