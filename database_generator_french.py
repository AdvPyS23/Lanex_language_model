import pandas as pd

# Create an empty DataFrame with the desired columns
vocabulary_list = pd.DataFrame(columns=["word", "translation", "pronunciation", "usage", "category", "difficulty"])

# Add some data to the DataFrame (example data)
data = [
    {"word": "apple", "translation": "pomme", "pronunciation": "ˈæpəl", "usage": "I ate an apple today.", "category": "fruits", "difficulty": "easy"},
    {"word": "house", "translation": "maison", "pronunciation": "haʊs", "usage": "This is my house.", "category": "buildings", "difficulty": "easy"},
    {"word": "car", "translation": "voiture", "pronunciation": "kɑr", "usage": "I have a red car.", "category": "vehicles", "difficulty": "easy"}
]

# Convert the data to a DataFrame
data_df = pd.DataFrame(data)

# Concatenate the data with the existing DataFrame
vocabulary_list = pd.concat([vocabulary_list, data_df], ignore_index=True)

# Save the DataFrame to a CSV file
vocabulary_list.to_csv("vocabulary_french.csv", index=False)

