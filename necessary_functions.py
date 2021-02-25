# Function lists_from_text creates a list of lists from an external file that takes 2 arguments,
# the first argument is the name of the file and the second argument is the separator of the elements in each list.
def lists_from_text(listx, line_sep):
    # Open the file and encode special characters.
    f = open(listx, "r", encoding='utf-8')

    # Create a list from the string in the file.
    list_of_lists = []
    for line in f:
        # Remove any white spaces before and after each line.
        stripped_line = line.strip()
        # Separate string in each line that become elements of each list.
        line_list = stripped_line.split(line_sep)
        # Add each list to a list of lists.
        list_of_lists.append(line_list)
    f.close()
    return list_of_lists

# Function reset removes all string in the external files that store words after using the trainer function.
def reset():
    correct_words = open('correctWords.txt', 'w', encoding='utf-8')
    correct_words.write('')
    wrong_words = open('wrongWords.txt', 'w', encoding='utf-8')
    wrong_words.write('')
