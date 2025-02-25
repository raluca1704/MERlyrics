
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

API_KEY = "Xv8XYOrEq2OlSeBWOnwZJWjkokc9zDAFuntmF_Q74ph802EyL6_q3YUuHh1SyTit"
BASE_URL = "https://api.genius.com"

def get_lyrics_with_selenium(url):
    options = Options()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = ChromeService(executable_path="C:/Users/raluc/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    browser = webdriver.Chrome(service=service, options=options)

    browser.get(url)

    try:

        lyrics_div = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "lyrics-root"))
        )
        lyrics = lyrics_div.text
    except Exception as e:
        print(f"Eroare: {e}")
        lyrics = "Versurile nu au putut fi extrase."

    browser.quit()
    return lyrics.strip()


with open("songs_data.json", "r", encoding="utf-8") as json_file:
    songs = json.load(json_file)

for song in songs:
    print(f"Extragem versurile pentru: {song['title']} - {song['artist']}")
    song["lyrics"] = get_lyrics_with_selenium(song["url"])


with open("song_lyrics.json", "w", encoding="utf-8") as json_file:
    json.dump(songs, json_file, indent=4, ensure_ascii=False)

print("Versurile au fost salvate în song_lyrics.json")
