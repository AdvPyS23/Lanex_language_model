# -*- coding: utf-8 -*-
"""
Created on Wed May 10 23:48:12 2023

@author: laura
"""

import random

# Idea: ask user for test duration short, medium or long

#works only for English so far
def lanex_quiz(word_list, category=None, difficulty=None):
    #determine amount of entries into the dataframe
    word_amount = word_list.shape[0]
    quiz_list = list(range(10))
    mark = []
    
    #print user instructions
    print('Welcome to you vocabulary test')
    print('For correct answers be sure to enter words capitalized')
    
    #improvement point: randomize the word selection
    
    #loop over words to test
    for i in range(3):
        word = word_list.English[i]
        sentence = 'What is the translation of ' + word + '? '
        answer = input(sentence)
        score = answer == word_list.Dutch[i]
        mark.append(score)
        grade = sum(mark)
    
    print(f'Your grade is {grade} out of 10')
    return grade

#use this to append to a database of grades
dutch_test_grade = lanex_quiz(start_df)
