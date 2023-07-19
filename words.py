#For a list of words, print out each word on a separate line, but in all uppercase.
def print_upper_words(words):
    """This function turns a list of submitted words wholly to uppercase"""
    for word in words:
        print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])

#Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).
def if_starts_with_e(words):
    """Accepts a list of words and prints only those words which start with the letter 'e'"""
    for word in words:
        if word[0].lower() == 'e':
            print(word)

if_starts_with_e(['excellent','egg', 'goodbye', 'yes', 'tree', 'extra'])

#Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.

def print_upper_words_2(words):
    """Accepts a list of words and prompts the user to enter letters to filter by, then prints only words that start with those letters"""
    filter_letters_input = input("Enter the letters separated by commas: ")
    input_list = [item.strip() for item in filter_letters_input.split(",")]
    filter_letters = set(input_list)
    
    for word in words:
        if word[0].lower() in filter_letters:
            print(word)

print_upper_words_2(["hello", "hey", "goodbye", "yo", "yes"])

