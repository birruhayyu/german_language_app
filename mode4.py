# Random module picks an element from a list randomly.
import random
# Function lists_from_text creates a list of lists from a text file.  It takes 2 arguments.
# The first argument is the name of the file and the second argument is the separator of the elements in each list.
from necessary_functions import lists_from_text

def madlibs():
    # Create a list of lists from the database text file.
    list_database = lists_from_text('words.txt', ', ')
    # Create separate lists from the data base file according to their types, (noun),(adj.),(verb).
    dbnoun = []
    dbadj = []
    dbverb = []
    for item in list_database:
        if item[1] == '(noun)':
            dbnoun.append(item)
        elif item[1] == '(adj.)':
            dbadj.append(item)
        else:
            dbverb.append(item)

    # Create a list of lists from the text file containing words the user already knows.
    # These words are taken from the file that stores words that the user translated correctly in the trainer mode.
    list_correct_words = lists_from_text('correctWords.txt', ', ')
    # Create separate lists from the words the user already knows according to their types, (noun),(adj.),(verb).
    correct_words_noun = []
    correct_words_adj = []
    correct_words_verb = []
    for item in list_correct_words:
        if item[1] == '(noun)':
            correct_words_noun.append(item)
        elif item[1] == '(adj.)':
            correct_words_adj.append(item)
        else:
            correct_words_verb.append(item)

    # Madlibs takes random English words from the list of words the user already knows if the number is sufficient.
    if len(correct_words_noun) >= 2 and len(correct_words_adj) > 2 and len(correct_words_verb) >= 2:
        print("A unicorn is nothing like a(n) '%s'. They're '%s' creatures. Some have a '%s' mane of hair "
              "and others have a(n) '%s' '%s' on their head. I would love '%s' a unicorn one day."
              % (random.choice(correct_words_noun)[-1], random.choice(correct_words_adj)[-1],
                 random.choice(correct_words_adj)[-1], random.choice(correct_words_adj)[-1],
                 random.choice(correct_words_noun)[-1], random.choice(correct_words_verb)[-1]))
    # Otherwise madlibs takes random English words from the database.
    else:
        print("A unicorn is nothing like a(n) '%s'. They're '%s' creatures. Some have a '%s' mane of hair "
              "and others have a(n) '%s' '%s' on their head. I would love '%s' a unicorn one day."
              % (random.choice(dbnoun)[-1], random.choice(dbadj)[-1], random.choice(dbadj)[-1],
                 random.choice(dbadj)[-1], random.choice(dbnoun)[-1], random.choice(dbverb)[-1]))


