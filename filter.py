import json
import re


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
    "its", "our", "their",
])


def filter_lyrics(lyrics):

    cleaned_lyrics = re.sub(r'^\d+\s+Contributors\n.*?\n', '', lyrics, flags=re.DOTALL)
    cleaned_lyrics = re.sub(r'\[Verse \d+\]', '', cleaned_lyrics)


    words = re.findall(r'\b\w+\b', cleaned_lyrics.lower())


    relevant_words = [word for word in words if word not in irrelevant_words and not word.isdigit()]
    return ' '.join(relevant_words)



with open("song_lyrics.json", "r", encoding="utf-8") as json_file:
    songs = json.load(json_file)


for song in songs:
    if "lyrics" in song:
        song["filtered_lyrics"] = filter_lyrics(song["lyrics"])

# Salvăm rezultatul într-un nou fișier JSON
with open("filtered_song_lyrics.json", "w", encoding="utf-8") as json_file:
    json.dump(songs, json_file, indent=4, ensure_ascii=False)

print("Versurile filtrate au fost salvate în filtered_song_lyrics.json")
