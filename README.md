Instructions:
1. Copy all the files on this folder on your PyCharm project.
2. Open your terminal in PyCharm.
3. Type 'python home.py' to run the program.
4. Follow the instructions.


Program Content:

1. 'Dictionary mode' is where the user can translate a word (German/ English).

2. 'Trainer mode' is where the user can train their German or English vocabulary. 
The words are taken from the external database called words.txt.
If the user answers correctly, the words are stored in an external file called correctWords.txt. 
If the user answers wrongly, the words are stored in an external file called wrongWords.txt.
If wrongWords.txt and correctWords.txt are filled with more than 2 pairs of words, 
the trainer mode will also display words from these files. 
The words that are displayed on the trainer mode are then the combination of these three files with a ratio:
(words.txt : wrongWords.txt : correctWords.txt) = (5 : 3: 1)

3. 'Analytics mode' is where the user can check their performance statistics after using the trainer mode. 
It calculates the words stored in the external files, correctWords.txt and wrongWords.txt.

4. 'Grammar mode' is where the user can check (pronoun + to-be) grammar in German.

5. 'Madlibs mode' is where the user can play madlibs games. 
The words are taken from correctWords.txt which stores words the user already knows. 
If it is not sufficient, the words are then taken from the database words.txt file.

