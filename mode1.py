# Lists_from_text function creates a list of lists from a text file.
from necessary_functions import lists_from_text

# Dictionary function takes one argument, the word to translate.  It returns the translated word.
def dictionary(word):
    # Create a list of lists from the database words.txt.  The second argument is the sign where to split each list.
    list_of_lists = lists_from_text('words.txt', ', ')

    # Iterate over list of lists to check if the word is in one of the lists.
    for line in list_of_lists:
        # If the word is in one of the lists.
        if word in line or word.lower() in [line[0].lower(),line[-1].lower()]:
            # If the word is the first element of the list, German, it returns the last element of the list, English.
            if word == line[0] or word.lower() == line[0].lower():
                print(line[-1] + line[1])
                break
            # If the word is the last element of the list, English, it returns the first element of the list, German.
            elif word.lower() == line[-1]:
                print(line[0] + line[1])
                break
        # Return a hint if the user translate an English verb, but missing 'to' at the beginning.
        if word.lower() == line[-1][3:]:
            print("'to " + word.lower() + "'" + ' means ' + line[0] + line[1])
            break
    # For any word that is not in the list of lists
    else:
        print(word + ' is not in the dictionary.')
