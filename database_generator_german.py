# -*- coding: utf-8 -*-
"""
Created on Fri May 19 19:41:09 2023

@author: laura
"""


import pandas as pd


# Create an empty DataFrame with the desired columns
vocabulary_list = pd.DataFrame(columns=["word", "translation", "pronunciation", "usage", "category", "difficulty"])

# Add some data to the DataFrame (example data)
# category: singular
data = [
    {"word": "hallo", "translation": "hello", "pronunciation": "halo", "usage": "Hallo, wie geht's?", "category": "greeting", "difficulty": "I"},
    {"word": "ja", "translation": "yes", "pronunciation": "jaː", "usage": "Ja, genau.", "category": "basic", "difficulty": "I"},
    {"word": "nein", "translation": "no", "pronunciation": "naɪ̯n", "usage": "Nein, bitte nicht.", "category": "basic", "difficulty": "I"},
    {"word": "danke", "translation": "thank you", "pronunciation": "daŋkə", "usage": "Danke für die Blumen.", "category": "basic", "difficulty": "I"},
    {"word": "links", "translation": "left", "pronunciation": "lɪŋks", "usage": "Nächste Ausfahrt links.", "category": "direction", "difficulty": "I"},
    {"word": "rechts", "translation": "rights", "pronunciation": "rɛçts", "usage": "Nächste Ausfahrt rechts.", "category": "direction", "difficulty": "I"},
    {"word": "tschüss", "translation": "bye", "pronunciation": "tʃʏs", "usage": "Bis bald. Tschüss.", "category": "parting", "difficulty": "I"},
    {"word": "schule", "translation": "school", "pronunciation": "ʃuːlə", "usage": "Ich gehe zur Schule.", "category": "education", "difficulty": "I"},
    {"word": "universität", "translation": "university", "pronunciation": "univɛɐ̯ziˈtɛːt", "usage": "Ich studiere an der Universität.", "category": "education", "difficulty": "II"},
    {"word": "bioinformatik", "translation": "bioinformatics", "pronunciation": "bijoɪnfɔʁˈmaːtɪk", "usage": "Ich studiere Bioinformatik.", "category": "education", "difficulty": "III"},
    {"word": "auto", "translation": "car", "pronunciation": "ɑuto", "usage": "Ich fahre das Auto.", "category": "vehicle", "difficulty": "II"}
]

# Convert the data to a DataFrame
data_df = pd.DataFrame(data)

# Concatenate the data with the existing DataFrame
vocabulary_list = pd.concat([vocabulary_list, data_df], ignore_index=True)

# Save the DataFrame to a CSV file
vocabulary_list.to_csv("vocabulary_german.csv", index=False, header=True)
