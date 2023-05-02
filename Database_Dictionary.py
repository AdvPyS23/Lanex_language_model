# Define an empty dictionary to store the words and their properties
vocab_dict = {}

# Loop to ask the user for input and store it in the dictionary
while True:
    word = input("Enter a vocabulary word (or 'q' to quit): ")
    if word == 'q':
        break
    translation = input("Enter the translation: ")
    pronunciation = input("Enter the pronunciation: ")
    usage = input("Enter an example of usage: ")
    category = input("Enter a category (topic/difficulty/part of speech): ")
    
    # Check if the category already exists in the dictionary
    if category in vocab_dict:
        vocab_dict[category][word] = {'translation': translation, 'pronunciation': pronunciation, 'usage': usage}
    else:
        vocab_dict[category] = {word: {'translation': translation, 'pronunciation': pronunciation, 'usage': usage}}

# Print the dictionary
print(vocab_dict)
