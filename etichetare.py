import pandas as pd

valence_arousal_dict = {
    "happy": (0.8, 0.8),  # Valence, Arousal
    "love": (0.9, 0.8),
    "cry": (0.1, 0.7),
    "hurt": (0.2, 0.5),
    "goodbye": (0.3, 0.7),
    "dance": (0.9, 0.8),
    "party": (0.9, 0.9),
    "dream": (0.7, 0.5),
    "remember": (0.5, 0.8),
    "lonely": (0.3, 0.2),

}


df = pd.read_csv("filtered_song_lyrics.csv")



def calculate_valence_arousal(lyrics):
    total_valence = 0
    total_arousal = 0
    count = 0

    for word in lyrics.split():
        if word in valence_arousal_dict:
            valence, arousal = valence_arousal_dict[word]
            total_valence += valence
            total_arousal += arousal
            count += 1

    if count > 0:
        avg_valence = total_valence / count
        avg_arousal = total_arousal / count
        return avg_valence, avg_arousal
    else:
        return None, None


df["valence"], df["arousal"] = zip(*df["filtered_lyrics"].apply(calculate_valence_arousal))

df.to_csv("filtered_song_lyrics_with_valence_arousal.csv", index=False)
print("Valorile Valence și Arousal au fost adăugate și salvate în filtered_song_lyrics_with_valence_arousal.csv")
