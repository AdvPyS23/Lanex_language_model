"""
This module defines the class Word,
which represents a word in the database,
that comes with definition, pronounciation, etc.
The Word class also has methods for
searching and testing the words.
"""
import tkinter as tk
import random
from tkinter import messagebox
import pandas as pd

# Define a class for vocabulary words
class Word:
    def __init__(self, word, translation, pronunciation, usage, category, difficulty):
        self.word = word
        self.translation = translation
        self.pronunciation = pronunciation
        self.usage = usage
        self.category = category
        self.difficulty = difficulty

# Create an empty DataFrame
vocabulary_list = pd.DataFrame(columns=[
    "word", "translation", "pronunciation", "usage", "category", "difficulty"])

# Define a function to add a new word to the vocabulary list
def add_word():
    word = word_entry.get()
    translation = translation_entry.get()
    pronunciation = pronunciation_entry.get()
    usage = usage_entry.get()
    category = category_entry.get()
    difficulty = difficulty_entry.get()
    new_word = Word(word, translation, pronunciation, usage, category, difficulty)
    global vocabulary_list
    vocabulary_list = vocabulary_list.append({"word": new_word.word,
                                              "translation": new_word.translation,
                                              "pronunciation": new_word.pronunciation,
                                              "usage": new_word.usage,
                                              "category": new_word.category,
                                              "difficulty": new_word.difficulty}, ignore_index=True)
    word_entry.delete(0, tk.END)
    translation_entry.delete(0, tk.END)
    pronunciation_entry.delete(0, tk.END)
    usage_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    status_label.config(text="New word added to database.", fg="green")
    root.after(2000, lambda: clear_status_label())

# Define a function to display all words in the vocabulary list
def display_words():
    word_list.delete(0, tk.END)
    for row in vocabulary_list.iterrows():
        word_list.insert(tk.END, row["word"])

# Define a function to search for a specific word in the vocabulary list
def search_word():
    """
    This function allows the user to search for their words
    in the database.
    """
    search_term = search_entry.get()
    found = False
    word_display.config(text="")  # Clear the previous displayed word
    for row in vocabulary_list.iterrows():
        if row[1]["word"] == search_term:
            word_display.config(
                text=
                "Word: {}\nTranslation: {}\nPronunciation: {}\nUsage: {}\nCategory: {}".format(
                    row[1]["word"], row[1]["translation"],
                    row[1]["pronunciation"], row[1]["usage"],
                    row[1]["category"]
                ),
                fg="black",
            )
            found = True
            break
    if not found:
        word_display.config(text="Word not found.", fg="red")
        
def clear_status_label():
    """
    This function clears the status_label text.
    """
    status_label.config(text="")

# ----------------------------------------------------------------------------------
# Testing
#----------------------------------------------------------------------------------
def start_test():
    """
    This function allows the user to start test their words by
    typing. This function is currently WIP.
    """
    # Select a random word from the vocabulary list
    test_word = random.choice(vocabulary_list)
    # Display the word in the test entry widget
    test_entry.config(state="normal")
    test_entry.delete(0, tk.END)
    test_entry.insert(0, test_word)
    test_entry.config(state="disabled")
    # Enable the submit button
    submit_button.config(state="normal")

def check_answer(answer, expected):
    """
    This function checks the answer.
    """
    if answer.lower() == expected.lower():
        messagebox.showinfo("Correct!")
    else:
        messagebox.showerror(f"Incorrect. The correct answer is {expected}.")

#===========================
# Define the main function
#===========================
def main():
    """
    This is the main function.
    """
    global vocabulary_list,word_entry
    global translation_entry
    global pronunciation_entry
    global usage_entry
    global category_entry
    global difficulty_entry
    global word_display
    global search_entry
    global status_label
    global word_list
    global test_entry
    global submit_button
    global root
    # Create the main window
    root = tk.Tk()
    root.title("Lanex: Your trusted Language Learning Assistant")


    # User interface: setting up the buttons
    # Word input
    word_label = tk.Label(root, text="Word:")
    word_label.grid(row=0, column=0)
    word_entry = tk.Entry(root)
    word_entry.grid(row=0, column=1)

    # Translation
    translation_label = tk.Label(root, text="Translation:")
    translation_label.grid(row=1, column=0)
    translation_entry = tk.Entry(root)
    translation_entry.grid(row=1, column=1)

    # Pronunciation
    pronunciation_label = tk.Label(root, text="Pronunciation:")
    pronunciation_label.grid(row=2, column=0)
    pronunciation_entry = tk.Entry(root)
    pronunciation_entry.grid(row=2, column=1)

    # Usage / Application
    usage_label = tk.Label(root, text="Usage:")
    usage_label.grid(row=3, column=0)
    usage_entry = tk.Entry(root)
    usage_entry.grid(row=3, column=1)

    # Category
    category_label = tk.Label(root, text="Category:")
    category_label.grid(row=4, column=0)
    category_entry = tk.Entry(root)
    category_entry.grid(row=4, column=1)
    # Difficulty
    difficulty_label = tk.Label(root,text = 'Difficulty')
    difficulty_label.grid(row=5, column = 0)
    options = ["Easy", "Moderate", "Hard"]
    difficulty_entry = tk.StringVar(root)
    difficulty_entry.set(options[0]) # default option 
    difficulty_menu = tk.OptionMenu(root, difficulty_entry, *options)
    difficulty_menu.grid(row=5, column=1)

    # Create the add word button
    add_button = tk.Button(root, text="Add Word", command=add_word)
    add_button.grid(row=6, column=1)

    # Create the display words button and listbox
    display_button = tk.Button(root, text="Display Words", command=display_words)
    display_button.grid(row=6, column=0)
    word_list = tk.Listbox(root)
    word_list.grid(row=7, column=1)

    # Create the search word widgets
    search_label = tk.Label(root, text="Search Word:")
    search_label.grid(row=8, column=0)
    search_entry = tk.Entry(root)
    search_entry.grid(row=8, column=1)
    search_button = tk.Button(root, text="Search by Words", command=search_word)
    search_button.grid(row=8, column=2)
    

    # Create the word display label
    word_display = tk.Label(root, text="", font=("Arial", 12))
    word_display.grid(row=9, column=0, columnspan=2)

    # Create the status label
    status_label = tk.Label(root, text="", font=("Arial", 12))
    status_label.grid(row=12, column=0, columnspan=2)
    # Get the test mode
    #Create the test mode button
    test_button = tk.Button(root, text="Test Mode", command=start_test)
    test_button.grid(row=15, column=0)
    # Create the test mode entry widget and submit button
    test_entry = tk.Entry(root)
    test_entry.grid(row=15, column=1)
    test_entry.config(state="disabled")
    submit_button = tk.Button(root, text="Submit",
                              command=lambda:
                                  check_answer(test_entry.get(), test_word))
    submit_button.grid(row=15, column=2)
    submit_button.config(state="disabled")

    # Create the start test button
    start_test_button = tk.Button(root,
                                  text="Start Test",
                                  command=start_test)
    start_test_button.grid(row=14, column=1)

    root.mainloop()

if __name__ == '__main__':
    main()