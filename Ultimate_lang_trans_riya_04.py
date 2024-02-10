'''
Program_Name: Ultimate Language Translation
Filename: Ultimate_lang_trans_riya_04.py
Author:  Riya Verma
Purpose: To translate across languages, the application will read from and write to a vocabulary file kept in the same folder.
Revisions:
        00 - Read the vocabulary list and compile dictionaries of both Italian and English terms.
        01 - Created the while loop for the language translation and also prints if the term is not found.
        02 - Finished the final language translation by improving the software and adding the words to the already-existing dictionary
'''

# Program Name Line
print('A user-interactive program for translating between English and Italian \n')

vocabulary_file = "vocabulary.txt"

# Read the vocabulary file and create dictionaries for English to Italian and Italian to English translations
with open(vocabulary_file, "r") as file:
    english_to_italian = {}
    italian_to_english = {}
    for line in file:
        line = line.strip().split("\t")
        english_to_italian[line[0]] = line[1]
        italian_to_english[line[1]] = line[0]

# Print the available English and Italian words
print("Available English words:")
for eng_word in english_to_italian.keys():
    print(eng_word)
print()

print("Available Italian words:")
for it_word in italian_to_english.keys():
    print(it_word)
print()

# Creating a continuous loop while the user keeps entering words
while True:
    word = input("Enter an English or Italian word (or press Enter to quit): ").lower()

    # If the user enters an empty string, the loop breaks and the program exits.
    if word == '':
        break

    # If the word is in the English dictionary, the program prints the translation in Italian
    if word in english_to_italian:
        translation = english_to_italian[word]
        print(f"The translation of {word} in Italian is {translation}\n")
    # If the word is in the Italian dictionary, the program prints the translation in English
    elif word in italian_to_english:
        translation = italian_to_english[word]
        print(f"The translation of {word} in English is {translation}\n")
    # If the word is not in either dictionary, the program asks the user if they want to add the word to the dictionary.
    else:
        add_word = input(f"{word} not found. Do you want to add it to the dictionary? (yes/no): ").lower()

        # If the user answers yes, the program asks for the language of the word (English or Italian) and the translation. The word and its translation are then added to the appropriate dictionaries and written to the vocabulary file.
        if add_word == 'yes':
            language = input("Is the word in English or Italian? ").lower()
            if language == 'english':
                translation = input("What is the Italian translation? ").lower()
                english_to_italian[word] = translation
                italian_to_english[translation] = word
                with open(vocabulary_file, "a") as file:
                    file.write(f"{word}\t{translation}\n")
                print(f"{word} has been added to the English dictionary with the Italian translation {translation}\n")
            elif language == 'italian':
                translation = input("What is the English translation? ").lower()
                italian_to_english[word] = translation
                english_to_italian[translation] = word
                with open(vocabulary_file, "a") as file:
                    file.write(f"{translation}\t{word}\n")
                print(f"{word} has been added to the Italian dictionary with the English translation {translation}\n")
            else:
                print("Invalid input. Please try again.")
        else:
            print(f"{word} not added to the dictionary.")
