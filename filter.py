import json
import re
import csv

irrelevant_words = set([
    "a", "an", "the", "and", "but", "or", "for", "nor", "on", "at", "to",
    "in", "with", "is", "are", "was", "were", "be", "been", "have",
    "has", "had", "do", "does", "did", "this", "that", "these", "those",
    "of", "by", "from", "it", "its", "if", "then", "else", "when",
    "where", "why", "what", "who", "whom", "which", "that", "there",
    "here", "not", "no", "yes", "so", "very", "just", "like", "also",
    "but", "only", "now", "up", "down", "out", "in", "about", "after",
    "before", "between", "during", "around", "with", "without", "all",
    "some", "any", "many", "few", "more", "most", "other", "another",
    "much", "less", "same", "such", "own", "my", "your", "his", "her",
    "its", "our", "their", "lyrics", "i", "ve",
])

def filter_lyrics(lyrics):
    cleaned_lyrics = re.sub(r'^\d+\s+Contributors\n.*?\n', '', lyrics, flags=re.DOTALL)
    cleaned_lyrics = re.sub(r'\[Verse \d+\]', '', cleaned_lyrics)

    words = re.findall(r'\b\w+\b', cleaned_lyrics.lower())

    relevant_words = [word for word in words if word not in irrelevant_words and not word.isdigit()]
    return ' '.join(relevant_words)

# Citește fișierul JSON
with open("song_lyrics.json", "r", encoding="utf-8") as json_file:
    songs = json.load(json_file)

# Scrie datele într-un fișier CSV
with open("filtered_song_lyrics.csv", "w", encoding="utf-8", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["title", "filtered_lyrics"])  # Header

    for song in songs:
        if "lyrics" in song:
            filtered_text = filter_lyrics(song["lyrics"])
            title = song.get("title", "Unknown Title")  # Asigurăm un titlu implicit dacă nu există
            csv_writer.writerow([title, filtered_text])

print("Versurile filtrate au fost salvate în filtered_song_lyrics.csv")
