from collections import Counter
# Function reset removes all string in the external files that store the words that the user have trained.
from necessary_functions import reset

# This function shows the number of correct and wrong answers from the trainer mode,
# the words the user answered correctly and incorrectly more than once, and the total number of trainings.
def analytics():
    total_training = 0
    # Open the external file that contains the correctly answered words and encode the special characters.
    correct_words = open('correctWords.txt', 'r', encoding='utf-8')
    # Make a list of lists from the external file.
    list_correct_words = []
    for line in correct_words:
        # Remove all unnecessary white spaces before and after the each line.
        stripped_line = line.strip()
        list_correct_words.append(stripped_line)

    # Make a dictionary of list_correct_words with the words as keys and their frequency as values.
    dict_correct_words = Counter(list_correct_words)
    print("Number of words you answered CORRECTLY: " + str(len(dict_correct_words)))

    # Find the words that the user answered correctly more than once.  This make the dictionary become a list of tuples.
    common_right_words = dict_correct_words.most_common()
    most_right_words = ()
    # Check the correct words that appear more than once, by checking the number on index 1 of each tuple.
    for item in common_right_words:
        if item[1] >= 2:
            # If a tuple appears more than once, add it on tuple most_right_words.
            most_right_words += item
    print("The words you answered CORRECTLY more than once: " + str(most_right_words))
    correct_words.close()

    # Open the external file that contains the wrongly answered words and encode the special characters.
    wrong_words = open('wrongWords.txt', 'r', encoding='utf-8')
    # Make a list of lists from the external file.
    list_wrong_words = []
    for line in wrong_words:
        # Remove all unnecessary white spaces before and after the each line.
        stripped_line = line.strip()
        list_wrong_words.append(stripped_line)

    # Make a dictionary of list_wrong_words with the words as keys and their frequency as values.
    dict_wrong_words = Counter(list_wrong_words)
    print("Number of words you answered WRONGLY: " + str(len(dict_wrong_words)))

    # Find the words that the user answered wrongly more than once.  This make the dictionary become a list of tuples.
    common_wrong_words = dict_wrong_words.most_common()
    most_wrong_words = ()
    # Check the wrong words that appear more than once, by checking the number on index 1 of each tuple.
    for item in common_wrong_words:
        if item[1] >= 2:
            # If a tuple appears more than once, add it on tuple most_wrong_words.
            most_wrong_words += item
    print("The words you answered WRONGLY more than once: " + str(most_wrong_words))
    wrong_words.close()

    # The total words in both external files shows the number of trainings the user have done.
    total_training = len(dict_correct_words) + len(dict_wrong_words)
    print("Number of words you HAVE TRAINED: "+ str(total_training) + '\n')

    # Give the user options whether to reset the statistics or add it to the next calculation.
    input_reset = input('Type "reset" to reset the statistics or type "continue" to continue using your progress: ')
    # Reset will remove all the string in the external files that store the words the user already trained.
    if input_reset == 'reset':
        print("The statistics will start from 0.")
        reset()
    else:
        print('The statistics is saved')
