import tkinter as tk
import random
from tkinter import messagebox
import pandas as pd
import os
import subprocess

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

def is_font_installed(font_name):
    # Run fc-list command and check if the font name is present in the output
    command = f"fc-list : family | grep -i {font_name}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    return result.returncode == 0

def install_fonts():
    font_name = "NotoSansCJK"

    if is_font_installed(font_name):
        print(f"The {font_name} font is already installed.")
    else:
        # Command to install NotoSansCJK font
        command = "sudo apt-get install -y fonts-wqy-microhei"

        # Execute the command
        subprocess.run(command, shell=True)
        print(f"The {font_name} font has been installed.")
# Define a function to add a new word to the vocabulary list
def add_word():
    init_word = word_entry.get()
    init_translation = translation_entry.get()
    init_pronunciation = pronunciation_entry.get()
    init_usage = usage_entry.get()
    init_category = category_entry.get()
    init_difficulty = difficulty_entry.get()
    
    global vocabulary_list
    new_word = pd.DataFrame({"word": [init_word],
                             "translation": [init_translation],
                             "pronunciation": [init_pronunciation],
                             "usage": [init_usage],
                             "category": [init_category],
                             "difficulty": [init_difficulty]})
    vocabulary_list = pd.concat([vocabulary_list, new_word], ignore_index=True)
    word_entry.delete(0, tk.END)
    translation_entry.delete(0, tk.END)
    pronunciation_entry.delete(0, tk.END)
    usage_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    status_label.config(text="New word added to database.", fg="green")
    root.after(2000, lambda: clear_status_label())
    vocabulary_list = pd.concat([vocabulary_list, new_word], ignore_index=True)
    vocabulary_list.to_csv("vocabulary_list.csv", index=False)

# Define a function to display all words in the vocabulary list
def initialize_database():
    global vocabulary_list
    vocabulary_list = pd.DataFrame(columns=["word", "translation", "pronunciation", "usage", "category", "difficulty"])

    db_option = db_entry.get()

    if db_option == "Chinese(simplified)/简体中文":
        new_data = pd.read_csv('./vocabulary_chinese_simp.csv')
    elif db_option == "French/Française":
        new_data = pd.read_csv("./vocabulary_french.csv")
    elif db_option == "Dutch/Nederlands":
        new_data = pd.read_csv("./vocabulary_dutch.csv")
    elif db_option == "German/Deutsch":
        new_data = pd.read_csv("./vocabulary_german.csv")
    elif db_option == "Customized set 1":
        if os.path.isfile("./vocabulary_cs1.csv"):
            new_data = pd.read_csv("./vocabulary_cs1.csv")
        else:
            new_data = pd.DataFrame(columns=["word", "translation", "pronunciation", "usage", "category", "difficulty"])
            new_data.to_csv("vocabulary_cs1.csv", index=False, header=True)
    else:  # Customized set 2:
        if os.path.isfile("./vocabulary_cs2.csv"):
            new_data = pd.read_csv("./vocabulary_cs2.csv")
        else:
            new_data = pd.DataFrame(columns=["word", "translation", "pronunciation", "usage", "category", "difficulty"])
            new_data.to_csv("vocabulary_cs2.csv", index=False, header=True)

    vocabulary_list = pd.concat([vocabulary_list, new_data], ignore_index=True)
    display_words()
    print(f"Checkpoint 1: vocabulary_list: {vocabulary_list}")
    return vocabulary_list



new_data = pd.read_csv("./vocabulary_french.csv")
print(f"Checkpoint 0.5: new_data: {new_data}")
def display_words():
    word_list.delete(0, tk.END)
    for index, row in vocabulary_list.iterrows():
        word_list.insert(tk.END, row["word"])


# Define a function to search for a specific word in the vocabulary list
def search_word():
    search_term = search_entry.get()
    search_results = vocabulary_list[vocabulary_list['word'] == search_term]
    if not search_results.empty:
        row = search_results.iloc[0]
        word_display.config(text=f"Word: {row['word']}\n"
                                 f"Translation: {row['translation']}\n"
                                 f"Pronunciation: {row['pronunciation']}\n"
                                 f"Usage: {row['usage']}\n"
                                 f"Category: {row['category']}\n"
                                 f"Difficulty: {row['difficulty']}")
    else:
        word_display.config(text="Word not found.")

    search_entry.delete(0, tk.END)
    
def search_word_difficulty():
    search_term = search_entry.get()
    search_results = vocabulary_list[vocabulary_list['difficulty'] == search_term]
    if not search_results.empty:
        row = search_results.iloc[0]
        word_display.config(text=f"Word: {row['word']}\n"
                                 f"Translation: {row['translation']}\n"
                                 f"Pronunciation: {row['pronunciation']}\n"
                                 f"Usage: {row['usage']}\n"
                                 f"Category: {row['category']}\n"
                                 f"Difficulty: {row['difficulty']}")
    else:
        word_display.config(text="Word not found.")

    search_entry.delete(0, tk.END)
        
def clear_status_label():
    """
    This function clears the status_label text.
    """
    status_label.config(text="")

def start_test():
    # Create a new window for the test
    global vocabulary_list
    blue = "#D49A89"  # pastel blue
    pink = "#557571"

    test_window = tk.Toplevel(root)
    test_window.title("Test Mode")
    test_window.config(bg=blue)

    # Get the test mode
    # Create the test mode label
    question_label = tk.Label(test_window, text="Question:")
    question_label.grid(row=0, column=0, padx=10, pady=10)

    # Create the test mode entry widget and submit button
    test_entry = tk.Entry(test_window)
    test_entry.grid(row=0, column=1, padx=10, pady=10)

    def check_answer():
        user_answer = test_entry.get().strip()
        correct_answer = vocabulary_list["translation"].iloc[0]
        if user_answer.lower() == correct_answer.lower():
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", f"Incorrect! The correct answer is: {correct_answer}")

    def ask_question_translation():
        # Select a random word from the vocabulary list
        question_word = random.choice(vocabulary_list["word"])
        correct_translation = vocabulary_list["translation"]

        # Set the question label text
        question_label.config(text=f"Question: Type in the translation of word: {question_word}")

        # Enable the entry and submit button
        test_entry.config(state="normal")
        submit_button.config(state="normal")

        # Clear the entry field
        test_entry.delete(0, tk.END)

        # Set focus on the entry field
        test_entry.focus_set()

    # Create the submit button
    submit_button = tk.Button(test_window, text="Submit", state="disabled", command=check_answer, bg=blue)
    submit_button.grid(row=0, column=2, padx=10, pady=10)

    # Bind the Enter key to the submit button
    test_window.bind('<Return>', lambda event: submit_button.invoke())

    # Disable the main window while the test window is open
    root.withdraw()

    # Event handler for closing the test window
    def close_test_window():
        test_window.destroy()
        root.deiconify()  # Re-enable the main window

    # Bind the close event of the test window to the close_test_window function
    test_window.protocol("WM_DELETE_WINDOW", close_test_window)

    # Start the test by asking the first question
    ask_question_translation()


def check_answer():
    answer = test_entry.get().strip()
    matches = vocabulary_list[vocabulary_list["word"] == answer]
    if not matches.empty:
        expected = matches["translation"].iloc[0]
        if answer.lower() == expected.lower():
            messagebox.showinfo("Well done!", "Your answer is correct!")
        else:
            messagebox.showerror("Nah-uh!", f"The correct answer is: {expected}")
    else:
        messagebox.showerror("Word not found", "The word is not found in the vocabulary list.")

#===========================
# Define the main function
#===========================
def main():
    """
    This is the main function.
    """
    global word_entry
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
    global db_entry
    
    # Create the main window
    # setting color theme:
    blue = "#D49A89" # pastel blue
    pink = "#557571" # paster pink
    yellow = "#FFFFE0" # pastel yellow
    root = tk.Tk()
    root.geometry("600x600") 
    root.configure(bg=pink)
    root.title("Lanex: Your trusted Language Learning Assistant")
    chinese_font = ("NotoSansCJK", 11)
    
    font_label = tk.Label(root, text = "Click to install fonts:",font = chinese_font, bg = pink)
    font_label.grid(row=0,column=0)
    install_button = tk.Button(root, text="Install Fonts", command=install_fonts, font = chinese_font,bg = blue)
    install_button.grid(row=0, column=1)
    
    # To begin Create the initialize database label
    activate_database_label = tk.Label(root, text = "Choose a dataset:",font = chinese_font,bg = pink)
    activate_database_label.grid(row = 1, column=0)
    activate_database = tk.Button(root, text="Activate this dataset", command=initialize_database,font=chinese_font,bg = blue)
    activate_database.grid(row = 2, column=1)
    db_options = ["French/Française", "Dutch/Nederlands", "Chinese(simplified)/简体中文", "German/Deutsch", "Customized set 1", "Customized set 2"]
    db_entry = tk.StringVar(root) 
    db_entry.set(db_options[0])
    db_menu = tk.OptionMenu(root, db_entry, *db_options)
    db_menu.config(font = chinese_font, bg=blue)
    db_menu.grid(row=1, column=1)

    # User interface: setting up the buttons
    # Word input
    word_label = tk.Label(root, text="Word:",font=chinese_font,bg = pink)
    word_label.grid(row=3, column=0)
    word_entry = tk.Entry(root)
    word_entry.grid(row=3, column=1)

    # Translation
    translation_label = tk.Label(root, text="Translation:",font =chinese_font,bg = pink)
    translation_label.grid(row=4, column=0)
    translation_entry = tk.Entry(root)
    translation_entry.grid(row=4, column=1)

    # Pronunciation
    pronunciation_label = tk.Label(root, text="Pronunciation:",font=chinese_font,bg = pink)
    pronunciation_label.grid(row=5, column=0)
    pronunciation_entry = tk.Entry(root)
    pronunciation_entry.grid(row=5, column=1)

    # Usage / Application
    usage_label = tk.Label(root, text="Usage:",font = chinese_font,bg = pink)
    usage_label.grid(row=6, column=0)
    usage_entry = tk.Entry(root)
    usage_entry.grid(row=6, column=1)

    # Category
    category_label = tk.Label(root, text="Category:",font = chinese_font,bg = pink)
    category_label.grid(row=7, column=0)
    category_entry = tk.Entry(root)
    category_entry.grid(row=7, column=1)
    
    # Difficulty
    difficulty_label = tk.Label(root,text = 'Difficulty:',font = chinese_font,bg = pink)
    difficulty_label.grid(row=8, column = 0)
    options = ["I", "II", "III"]
    difficulty_entry = tk.StringVar(root)
    difficulty_entry.set(options[0]) # default option 
    difficulty_menu = tk.OptionMenu(root, difficulty_entry, *options)
    difficulty_menu.grid(row=8, column=1)
    difficulty_menu.config(font = chinese_font)

    # Create the add word button
    add_button = tk.Button(root, text="Add to current dataset", command=add_word,font = chinese_font,bg=blue)
    add_button.grid(row=9, column=1)

    # Create the display words button and listbox
    #display_button = tk.Button(root, text="Display Words", command=display_words,font=chinese_font,bg=blue)
    #display_button.grid(row=11, column=0)
    word_list = tk.Listbox(root, font=chinese_font)
    word_list.grid(row=15, column=1)

    # -----------------------------------------------------------------------
    # Create the search word widgets
    search_label = tk.Label(root, text="Search words:",font = chinese_font,bg = pink)
    search_label.grid(row=14, column=0)
    search_entry = tk.Entry(root)
    search_entry.grid(row=14, column=1, sticky="ew", columnspan=1)
    search_button = tk.Button(root, text="Search Words", command=search_word, font = chinese_font,bg=blue)
    search_button.grid(row=14, column=0, sticky="ew")
    
    # search by difficulty
    search_difficulty_button = tk.Button(root, text = "Search Difficulty",command=search_word_difficulty, font = chinese_font,bg=blue)
    search_difficulty_button.grid(row=15, column=0,sticky="ew")
    
    

    # Create the word display label
    word_display = tk.Label(root, text="", font=chinese_font,bg = pink)
    word_display.grid(row=17, column=6, columnspan=2)

    # Create the status label
    status_label = tk.Label(root, text="", font=chinese_font,bg = pink)
    status_label.grid(row=12, column=3, columnspan=2)
    
    # Test interface:
    start_test_label = tk.Label(root, text = "Begin Testing", bg=pink)
    start_test_label.grid(row = 8, column = 6,columnspan=2)

    # Create the start test button
    start_test_button = tk.Button(root, text="Start Test", command=start_test, bg=blue, font=chinese_font)
    start_test_button.grid(row=12, column=6,columnspan=3)
    

    root.mainloop()
if __name__ == '__main__':
    main()
