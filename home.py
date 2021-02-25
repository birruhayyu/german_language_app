from mode1 import dictionary
from mode2 import trainer
from analytics import analytics
from mode3 import grammar
from mode4 import madlibs

# This function acts as a switching method between modes.
def switch():
    print('')
    print('You are HOME')
    print("*** Type ´dictionary´ to translate a word")
    print("*** Type ´trainer´ to train your vocabulary")
    print("*** Type ´analytics´ to check your vocabulary training analytics")
    print("*** Type ´grammar´ to practice your grammar")
    print("*** Type ´madlibs´ to play madlibs game")
    print("*** Type ´quit´ to quit the program \n")
    mode = input("Choose a mode: ")

    # Keep the program running until the user types 'quit'.
    while mode != 'quit':
        if mode == 'dictionary':
            print("You are on DICTIONARY mode. Type ´goHome´ to go back to home.")
            # Iterate the dictionary mode until the user types 'goHome'.
            while True:
                # Ask for the word to translate.
                word = input('Translate this word: ')
                # Translate the word.
                if word != 'goHome':
                    dictionary(word)
                # Stop the iteration if the user types 'goHome'.
                else:
                    break
            # Back to switch function.
            switch()

        elif mode == 'trainer':
                while trainer() != False:
                    trainer()
                switch()

        elif mode == 'analytics':
            print("You are on ANALYTICS mode." + '\n')
            analytics()
            # Back to switch function after quitting the analytics mode.
            switch()

        elif mode == 'madlibs':
            print("You are on MADLIBS mode. Type 'yes' to play or type 'goHome' to go back to home.")
            # Iterate the madlibs mode until the user types 'goHome'.
            while True:
                play = input("Play madlibs (yes/no)? " + "\n")
                if play == 'yes':
                    madlibs()
                else:
                    break
            switch()

        elif mode == 'grammar':
            print("You are in GRAMMAR mode. Type 'goHome' to go back to home.")
            # Iterate the grammar mode until the user types 'goHome'.
            while True:
                user_input = input("Type a sentence in German (pronoun + to be + adj(optional)): ")
                if user_input != 'goHome':
                    grammar(user_input)
                else:
                    break
            switch()
        # A message if the user does not type a correct keyword
        else:
            print('Type the correct name of the mode!')
            switch()
        break

switch()
