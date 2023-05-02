# -*- coding: utf-8 -*-
"""
Created on Mon May  1 10:29:14 2023

@author: laura
"""

import pandas as pd

#Basic set-up for database to start with 10 words

en_nl_dict = {"Hello": "Hallo", "Yes": "Ja", "No": "Nee", "Thank you": "Bedankt", "Left": "Links", "Right": "Rechts", "Bye": "Doei", "School": "School", "University": "Universiteit", "Bioinformatics": "Bioinformatica"}
en_nl_basic = pd.Series(en_nl_dict)

cat_dict = {"Hello": "Basics", "Yes": "Basics", "No": "Basics", "Thank you": "Basics", "Left": "Directions", "Right": "Directions", "Bye": "Basics", "School": "School", "University": "School", "Bioinformatics": "School"}
cat_ser = pd.Series(cat_dict)

start_df = pd.DataFrame({"Dutch": en_nl_basic, "Category": cat_ser})
#to make sure that the indeces are numbered and not the matching word
start_df.reset_index(inplace=True)
start_df = start_df.rename(columns = {'index':'English'})

#%%
#Create input code
#add to existing dataframe

new_en = input("What word would you like to enter? ")
new_nl = input("What is the translation of this new word? ")
#make a drop-down for this input
new_cat = input("In which category does it belong? ")

#construct new series
new_row = {"English": new_en,"Dutch" : new_nl, "Category": new_cat}

#add new series to dataframe
start_df = start_df.append(new_row, ignore_index=True)