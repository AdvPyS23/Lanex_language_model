# -*- coding: utf-8 -*-
"""
Created on Fri May 19 19:13:48 2023

@author: laura
"""


import pandas as pd


# Create an empty DataFrame with the desired columns
vocabulary_list = pd.DataFrame(columns=["word", "translation", "pronunciation", "usage", "category", "difficulty"])

# Add some data to the DataFrame (example data)
# category: singular
data = [
    {"word": "hallo", "translation": "hello", "pronunciation": "halo", "usage": "Hallo, hoe gaat het?", "category": "greeting", "difficulty": "I"},
    {"word": "ja", "translation": "yes", "pronunciation": "ja", "usage": "Ja, ik ben het ermee eens.", "category": "basic", "difficulty": "I"},
    {"word": "nee", "translation": "no", "pronunciation": "ne", "usage": "Nee, dat hoef ik niet.", "category": "basic", "difficulty": "I"},
    {"word": "bedankt", "translation": "thank you", "pronunciation": "bədɑŋkt", "usage": "Bedankt voor de bloemen.", "category": "basic", "difficulty": "I"},
    {"word": "links", "translation": "left", "pronunciation": "lɪŋks", "usage": "Volgende afslag naar links.", "category": "direction", "difficulty": "I"},
    {"word": "rechts", "translation": "rights", "pronunciation": "rɛx(t)s", "usage": "Ik schrijf met rechts.", "category": "direction", "difficulty": "I"},
    {"word": "doei", "translation": "bye", "pronunciation": "duj", "usage": "Tot de volgende keer. Doei.", "category": "parting", "difficulty": "I"},
    {"word": "school", "translation": "school", "pronunciation": "sxol", "usage": "Ik zit op school.", "category": "education", "difficulty": "I"},
    {"word": "universiteit", "translation": "university", "pronunciation": "ynivɛrsi'tɛit", "usage": "Ik studeer aan de universiteit.", "category": "education", "difficulty": "II"},
    {"word": "bioinformatica", "translation": "bioinformatics", "pronunciation": "bijoɪnfɔrˈmatika", "usage": "Ik studeer Bioinformatica.", "category": "education", "difficulty": "III"},
    {"word": "auto", "translation": "car", "pronunciation": "ɑuto", "usage": "Ik rij in de auto.", "category": "vehicle", "difficulty": "II"}
]

# Convert the data to a DataFrame
data_df = pd.DataFrame(data)

# Concatenate the data with the existing DataFrame
vocabulary_list = pd.concat([vocabulary_list, data_df], ignore_index=True)

# Save the DataFrame to a CSV file
vocabulary_list.to_csv("vocabulary_dutch.csv", index=False, header=True)