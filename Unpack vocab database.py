# -*- coding: utf-8 -*-
"""
Created on Tue May 16 15:50:59 2023

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
vocabulary_list.to_csv("//wsl.localhost/Ubuntu/home/laura--force-badname/adv_python_project/remote_clone/vocabulary_german.csv", index=False, header=True)

#%%
# generator for dutch

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
vocabulary_list.to_csv("//wsl.localhost/Ubuntu/home/laura--force-badname/adv_python_project/remote_clone/vocabulary_dutch.csv", index=False, header=True)

#%%
 # Construct the databases and save the locally to .csv files.

def german_vocab():
    #German vocabulary dataset
    en_de_dict = {"Hello": "Hallo", "Yes": "Ja", "No": "Nein", "Thank you": "Danke", "Left": "Links", "Right": "Rechts", "Bye": "Tschüss", "School": "Schule", "University": "Universität", "Bioinformatics": "Bioinformatik"}
    en_de_basic = pd.Series(en_de_dict)
    
    cat_dict = {"Hello": "Basic", "Yes": "Basic", "No": "Basic", "Thank you": "Basic", "Left": "Direction", "Right": "Direction", "Bye": "Basic", "School": "School", "University": "School", "Bioinformatics": "School"}
    cat_ser = pd.Series(cat_dict)
    
    en_de_data = pd.DataFrame({"German": en_de_basic, "Category": cat_ser})
    #to make sure that the indeces are numbered and not the matching word
    en_de_data.reset_index(inplace=True)
    en_de_data = en_de_data.rename(columns = {'index':'English'})
    
    #add columns for difficulty, usage and pronounciation
    #difficulty
    diff = ["I","I","I","I","I","I","I","I","II", "III"]
    en_de_data['Difficulty'] = diff
    #phonetic pronounciation
    phon_de = ["halo", "jaː", "naɪ̯n", "daŋkə", "lɪŋks", "rɛçts", "tʃʏs", "ʃuːlə", "univɛɐ̯ziˈtɛːt", "bijoɪnfɔʁˈmaːtɪk"]
    en_de_data['Pronounciation'] = phon_de
    #usage example
    use_de = ["Hallo, wie geht's?", "Ja, genau", "Nein, bitte nicht", "Danke für die Blumen", "Nächste Ausfahrt links", "Nächste Ausfahrt rechts", "Bis bald. Tschüss", "Ich gehe zur Schule", "Ich studiere an der Universität", "Ich studiere Bioinformatik"]
    en_de_data['Usage'] = use_de
    #save locally to .csv file
    en_de_data.to_csv("//wsl.localhost/Ubuntu/home/laura--force-badname/adv_python_project/remote_clone/vocabulary_german.csv")
    
def dutch_vocab():
    #Dutch vocabulary dataset
    en_nl_dict = {"Hello": "Hallo", "Yes": "Ja", "No": "Nee", "Thank you": "Bedankt", "Left": "Links", "Right": "Rechts", "Bye": "Doei", "School": "School", "University": "Universiteit", "Bioinformatics": "Bioinformatica"}
    en_nl_basic = pd.Series(en_nl_dict)
    
    cat_dict = {"Hello": "Basics", "Yes": "Basics", "No": "Basics", "Thank you": "Basics", "Left": "Directions", "Right": "Directions", "Bye": "Basics", "School": "School", "University": "School", "Bioinformatics": "School"}
    cat_ser = pd.Series(cat_dict)
    
    en_nl_data = pd.DataFrame({"Dutch": en_nl_basic, "Category": cat_ser})
    #to make sure that the indeces are numbered and not the matching word
    en_nl_data.reset_index(inplace=True)
    en_nl_data = en_nl_data.rename(columns = {'index':'English'})
    
    #add columns for difficulty, usage and pronounciation
    diff = ["I","I","I","I","I","I","I","I","II", "III"]
    en_nl_data['Difficulty'] = diff
    #phonetic pronounciation
    phon_nl = ["hɑlo", "ja", "ne", "bədɑŋkt", "lɪŋks", "rɛx(t)s", "duj", "sxol", "ynivɛrsi'tɛit", "bijoɪnfɔrˈmatika"]
    en_nl_data['Pronounciation'] = phon_nl
    #add usage example
    use_nl = ["Hallo, hoe gaat het?", "Ja, ik ben het ermee eens", "Nee, dat hoef ik niet", "Bedankt voor de bloemen", "Volgende afslag naar links", "Ik schrijf met rechts", "Tot de volgende keer. Doei", "Ik zit op school", "Ik studeer aan de universiteit", "Ik studeer Bioinformatica"]
    en_nl_data['Usage'] = use_nl
    #save locally to .csv file
    en_nl_data.to_csv("//wsl.localhost/Ubuntu/home/laura--force-badname/adv_python_project/remote_clone/vocabulary_dutch.csv")

#//wsl.localhost/Ubuntu/home/laura--force-badname/adv_python_project/remote_clone