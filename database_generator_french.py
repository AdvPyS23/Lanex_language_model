import pandas as pd

# Create an empty DataFrame with the desired columns
vocabulary_list = pd.DataFrame(columns=["word", "translation", "pronunciation", "usage", "category", "difficulty"])

# Add some data to the DataFrame (example data)
# category: singular
data = [
    {"word": "pomme", "translation": "apple", "pronunciation": "pɔm", "usage": "J'ai mangé une pomme aujourd'hui.", "category": "fruit", "difficulty": "I"},
    {"word": "maison", "translation": "house", "pronunciation": "mɛ.zɔ̃", "usage": "J'ai une maison.", "category": "building", "difficulty": "I"},
    {"word": "voiture", "translation": "car", "pronunciation": "vwɑˈtjʊə(ɹ)", "usage": "J'ai une voiture rouge.", "category": "vehnicle", "difficulty": "I"},
    {"word": "poisson", "translation": "fish", "pronunciation": "pwa.sɔ̃", "usage": "Je n'aime pas manger du poisson.", "category": "vehnicle", "difficulty": "I"},
    {"word": "banane", "translation": "banana", "pronunciation": "ba.nan", "usage": "J'ai acheté une banane au marché.", "category": "fruit", "difficulty": "I"},
    {"word": "orange", "translation": "orange", "pronunciation": "ɔ.ʁɑ̃ʒ", "usage": "Elle a pressé une orange pour faire du jus.", "category": "fruit", "difficulty": "I"},
    {"word": "mangue", "translation": "mango", "pronunciation": "mɑ̃ɡ", "usage": "La mangue est un fruit exotique très savoureux.", "category": "fruit", "difficulty": "III"}
    {"word": "pêche", "translation": "peach", "pronunciation": "pɛʃ", "usage": "Il a mangé une pêche juteuse.", "category": "fruit", "difficulty": "II"},
    {"word": "framboise", "translation": "raspberry", "pronunciation": "fʁɑ̃bwaz", "usage": "Elle a préparé une tarte aux framboises.", "category": "fruits", "difficulty": "III"},
    {"word": "chat", "translation": "cat", "pronunciation": "ʃa", "usage": "Le chat dort sur le canapé.", "category": "animal", "difficulty": "I"},
    {"word": "livre", "translation": "book", "pronunciation": "livʁ", "usage": "J'ai acheté un nouveau livre à la librairie.", "category": "education", "difficulty": "II"}
]

# Convert the data to a DataFrame
data_df = pd.DataFrame(data)

# Concatenate the data with the existing DataFrame
vocabulary_list = pd.concat([vocabulary_list, data_df], ignore_index=True)

# Save the DataFrame to a CSV file
vocabulary_list.to_csv("vocabulary_french.csv", index=False, header=True)

