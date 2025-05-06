import string
alphabet = string.ascii_lowercase + string.punctuation + " "

def count_words(text):
    #returns number of words in text
    words = text.split()
    return len(words)

def character_counter(text):
    #returns dictionary with lowercase letters and counts
    text = text.lower()  # Convert the entire text to lowercase
    letter_count = {}
    for letter in alphabet:
        count = text.count(letter)  # Count occurrences of the letter
        if count > 0:  # Only include letters that appear in the text
            letter_count[letter] = count
    return letter_count