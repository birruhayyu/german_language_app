# re checks a regular expression inside a string
import re

# Function grammar checks the correct sequence of pronoun + to-be in German. It takes a string as an argument.
def grammar(user_input):
    # Find any white space as a regular expression in the user_input, split them, and create a list.
    sentence = re.split('\s+', user_input)
    sentence = [element.lower() for element in sentence]
    # Create a dictionary with pronouns as keys and to-be(s) as values.
    german_grammar_dict = {'ich': 'bin', 'du': 'bist', 'er': 'ist', 'sie': 'ist', 'es': 'ist', 'wir': 'sind', 'ihr': 'seid'}
    # Check if any keys in german_grammar_dict presents in the list sentence.
    for pronoun in german_grammar_dict:
        # Make a different rule for pronoun 'sie' because it has more values than other pronouns.
        if pronoun in sentence and pronoun != sentence[-1]:
            if pronoun == 'sie':
                # Print 'Correct' if the element after 'sie' in list sentence is the correct to-be.
                if sentence[sentence.index(pronoun) + 1] == 'sind' or sentence[sentence.index(pronoun) + 1] == 'ist':
                    print('Correct')
                    break
                # Correct the grammar if the element after 'sie' in list sentence is not the correct to-be.
                else:
                    print('The correct answer is sie ' + '"ist" (third singular)' + ' ' +
                          ' or sie "sind" (third plural).')
                    break
            # Print 'Correct' if the element after pronoun in list sentence is the correct value of the pronoun.
            else:
                if sentence[sentence.index(pronoun)+1] == german_grammar_dict[pronoun]:
                    print('Correct')
                    break
                else:
                    print('The correct answer is '+ pronoun + ' '+ german_grammar_dict[pronoun] +'.')
                break
        # For other user_input that does not contain any pronouns.
    else:
        print('Please put the correct sentence sequence')
