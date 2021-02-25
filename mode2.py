import random
# Lists_from_text function creates a list of lists from an external file.
from necessary_functions import lists_from_text

# Randomizer function takes a list of lists as an input, displays a random word from that list, asks for user's answer,
# and evaluate the answer.
def randomizer(list_of_lists):
    # Get a random list from the list of lists.
    random_list = random.choice(list_of_lists)
    # Get a random item (word in English or German) from random list. Excluding the second element,(noun),(adj.),(verb).
    random_item = random.choice([random_list[0], random_list[-1]])
    # Get the correct translation of the random item. The correct translation is the other element in the list.
    correct_answer = []
    # If the random item is a German word, ask user for a translation in English.
    if random_item == random_list[0]:
        ans = input("'" + random_item + "'" + " in English is? ")
        correct_answer = random_list[-1]
    # If the random item is an English word, ask user for a translation in German.
    else:
        ans = input("'" + random_item + "'" + " in German is? ")
        correct_answer = random_list[0]
    # If the answer matches the correct_answer, the randomized list is added to an external file correctWords.txt.
    if ans.lower() == correct_answer or ans.lower() == correct_answer.lower():
        correct_list = open('correctWords.txt', 'a', encoding='utf-8')
        # Write all words from the random list.
        correct_list.write(random_list[0] + ', ' + random_list[1] + ', ' + random_list[-1] + '\n')
        print("Correct!")
    # If the answer does not match the correct_answer, the randomized list is added to an external file wrongWords.txt.
    else:
        wrong_list = open('wrongWords.txt', 'a', encoding='utf-8')
        # Write all words from the random list.
        wrong_list.write(random_list[0] + ', ' + random_list[1] + ', ' + random_list[-1] + '\n')
        print('The correct answer is ' + correct_answer)
    return ans


# This function displays random words from list_database 5 times, from wrong_list 3 times, and from correct_list 1 time.
def trainer():
    list_database = lists_from_text('words.txt', ', ')
    wrong_list = lists_from_text('wrongWords.txt', ', ')
    correct_list = lists_from_text('correctWords.txt', ', ')

    list_sources = [list_database, list_database, list_database, list_database, list_database, wrong_list, wrong_list,
                    wrong_list, correct_list]
    test = True
    for source in list_sources:
        if len(source) > 2:
            data = randomizer(source)
            if data != 'goHome':
                test = True
            else:
                test = False
                break
        # Skip sources that have less than 3 lists.
        else:
            continue
    return test
