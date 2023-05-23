# -*- coding: utf-8 -*-
"""
Created on Fri May 19 18:35:01 2023

@author: laura
"""

import matplotlib.pyplot as plt
import pandas as pd

#should be the score the test_function keeps track of
score = input('What was the score? ')
#should be adjusted to the database we keep of the score
score_list = [5,8,6,9,6,7,10]
wrong = 10 - int(score)

#labels for pie chart
labels = 'Correct', 'Wrong'
sizes = score, wrong

#plot piechart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['green', 'red'])
plt.show()

# I think we need the plot as an image in order to integrate it in interface
# Change path to the terminal home folder
plt.savefig("//wsl.localhost/Ubuntu/home/laura--force-badname/adv_python_project/score_plot.png")


#Make barplot of scores from last attempts.

#for some reason gives errors if I do it this way
# but we do need this method at some point.
#score_list.append(score)
attempts = list(range(1,len(score_list)+1))

#the bar plot gets quite messed up, but idk why
#too messed up to save yet
plt.bar(attempts, score_list)
plt.xlabel('Latest attempts')
plt.ylabel('Score')
plt.title('Progress')
plt.show()