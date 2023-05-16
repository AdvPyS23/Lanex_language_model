# -*- coding: utf-8 -*-
"""
Created on Tue May 16 15:50:59 2023

@author: laura
"""

import pandas as pd

 # Construct the databases and save the locally to .csv files.

#Maybe idea to ask user for path to directory and then add filename ourselves?
#ask just for the directory and then concatenats the string with the standard filename we set, user does not have to see this
filepath_laura_de = 'C:/Users/laura/OneDrive/Documenten/Bern/Universiteit/FS2023/473540_Advanced Python/Project/EN-DE.csv'
filepath_laura_nl = 'C:/Users/laura/OneDrive/Documenten/Bern/Universiteit/FS2023/473540_Advanced Python/Project/EN-NL.csv'

def german_vocab(filepath):
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
    en_de_data.to_csv(filepath)
    
def dutch_vocab(filepath):
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
    #difficulty, order is same as in German so reuse same code
    en_nl_data['Difficulty'] = diff
    #phonetic pronounciation
    phon_nl = ["hɑlo", "ja", "ne", "bədɑŋkt", "lɪŋks", "rɛx(t)s", "duj", "sxol", "ynivɛrsi'tɛit", "bijoɪnfɔrˈmatika"]
    en_nl_data['Pronounciation'] = phon_nl
    #add usage example
    use_nl = ["Hallo, hoe gaat het?", "Ja, ik ben het ermee eens", "Nee, dat hoef ik niet", "Bedankt voor de bloemen", "Volgende afslag naar links", "Ik schrijf met rechts", "Tot de volgende keer. Doei", "Ik zit op school", "Ik studeer aan de universiteit", "Ik studeer Bioinformatica"]
    en_nl_data['Usage'] = use_nl
    #save locally to .csv file
    en_nl_data.to_csv(filepath)

