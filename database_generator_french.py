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
    {"word": "mangue", "translation": "mango", "pronunciation": "mɑ̃ɡ", "usage": "La mangue est un fruit exotique très savoureux.", "category": "fruit", "difficulty": "III"},
    {"word": "pêche", "translation": "peach", "pronunciation": "pɛʃ", "usage": "Il a mangé une pêche juteuse.", "category": "fruit", "difficulty": "II"},
    {"word": "framboise", "translation": "raspberry", "pronunciation": "fʁɑ̃bwaz", "usage": "Elle a préparé une tarte aux framboises.", "category": "fruits", "difficulty": "III"},
    {"word": "chat", "translation": "cat", "pronunciation": "ʃa", "usage": "Le chat dort sur le canapé.", "category": "animal", "difficulty": "I"},
    {"word": "livre", "translation": "book", "pronunciation": "livʁ", "usage": "J'ai acheté un nouveau livre à la librairie.", "category": "education", "difficulty": "II"},
    {"word": "merci", "translation": "thank you", "pronunciation": "mɛʁ.si", "usage": "Merci beaucoup pour votre aide.", "category": "expression", "difficulty": "I"},
    {"word": "chien", "translation": "dog", "pronunciation": "ʃjɛ̃", "usage": "J'ai un chien qui s'appelle Max.", "category": "animal", "difficulty": "I"},
    {"word": "pain", "translation": "bread", "pronunciation": "pɛ̃", "usage": "Je vais acheter du pain à la boulangerie.", "category": "food", "difficulty": "I"},
    {"word": "soleil", "translation": "sun", "pronunciation": "sɔ.lɛj", "usage": "Le soleil brille aujourd'hui.", "category": "nature", "difficulty": "I"},
    {"word": "voiture", "translation": "car", "pronunciation": "vwa.tyʁ", "usage": "J'ai acheté une nouvelle voiture.", "category": "vehicle", "difficulty": "I"},
    {"word": "amour", "translation": "love", "pronunciation": "a.muʁ", "usage": "L'amour est un sentiment puissant.", "category": "emotion", "difficulty": "I"},
    {"word": "plage", "translation": "beach", "pronunciation": "plaʒ", "usage": "J'aime passer mes vacances à la plage.", "category": "location", "difficulty": "I"},
    {"word": "orthophoniste", "translation": "speech therapist", "pronunciation": "ɔʁ.tɔ.fɔ.nist", "usage": "Mon fils voit un orthophoniste pour améliorer sa parole.", "category": "profession", "difficulty": "III"},
    {"word": "avocat", "translation": "lawyer", "pronunciation": "a.vo.ka", "usage": "Mon père est avocat et il plaide dans les tribunaux.", "category": "profession", "difficulty": "III"},
    {"word": "architecte", "translation": "architect", "pronunciation": "aʁ.ʃi.tɛkt", "usage": "L'architecte a conçu un bâtiment moderne et innovant.", "category": "profession", "difficulty": "III"},
    {"word": "pilote", "translation": "pilot", "pronunciation": "pi.lɔt", "usage": "Le pilote a réussi à atterrir en toute sécurité.", "category": "profession", "difficulty": "III"},
    {"word": "professeur", "translation": "professor", "pronunciation": "pʁɔ.fɛ.sœʁ", "usage": "Le professeur donne un cours de mathématiques.", "category": "profession", "difficulty": "III"},
    {"word": "consultant", "translation": "consultant", "pronunciation": "kɔ̃.syl.tɑ̃", "usage": "La société a engagé un consultant pour améliorer ses opérations.", "category": "profession", "difficulty": "III"},
    {"word": "restaurant", "translation": "restaurant", "pronunciation": "ʁɛs.to.ʁɑ̃", "usage": "Allons dîner dans un bon restaurant ce soir.", "category": "place", "difficulty": "II"},
    {"word": "restaurant", "translation": "restaurant", "pronunciation": "ʁɛs.to.ʁɑ̃", "usage": "Allons dîner dans un bon restaurant ce soir.", "category": "place", "difficulty": "II"},
    {"word": "médecin", "translation": "doctor", "pronunciation": "me.də.sɛ̃", "usage": "Le médecin m'a prescrit des médicaments.", "category": "profession", "difficulty": "II"},
    {"word": "journal", "translation": "newspaper", "pronunciation": "ʒuʁ.nal", "usage": "Je lis le journal tous les matins.", "category": "object", "difficulty": "II"},
    {"word": "fenêtre", "translation": "window", "pronunciation": "fə.nɛtʁ", "usage": "Ouvre la fenêtre, s'il te plaît.", "category": "object", "difficulty": "II"},
    {"word": "hôpital", "translation": "hospital", "pronunciation": "o.pi.tal", "usage": "Ma grand-mère est à l'hôpital.", "category": "location", "difficulty": "II"},
    {"word": "maison", "translation": "house", "pronunciation": "mɛ.zɔ̃", "usage": "J'ai acheté une nouvelle maison.", "category": "location", "difficulty": "II"},
    {"word": "voyager", "translation": "to travel", "pronunciation": "vwa.ja.ʒe", "usage": "Je veux voyager à travers le monde.", "category": "verb", "difficulty": "II"},
    {"word": "écrire", "translation": "to write", "pronunciation": "e.kʁiʁ", "usage": "J'aime écrire des histoires.", "category": "verb", "difficulty": "II"}
]

# Convert the data to a DataFrame
data_df = pd.DataFrame(data)

# Concatenate the data with the existing DataFrame
vocabulary_list = pd.concat([vocabulary_list, data_df], ignore_index=True)

# Save the DataFrame to a CSV file
vocabulary_list.to_csv("vocabulary_french.csv", index=False, header=True)

