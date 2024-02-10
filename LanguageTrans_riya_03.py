'''
Filename: LanguageTrans_riya_03.py
Author:   Riya Verma
Purpose:  This program translates word from English to Italian and vice-versa .
Revision:
      00: Creating List and asking user for word.
      01: Checking if the input is in English list or Italian list and printting result accordingly
      03: If a new word is added, appending to the word list for both languages
      02: if the word is in neither list, printing a message
'''
print('Program to translate word from English to Italian and vice-versa\n')

# Initialize English and Italian word lists
english = ['sun', 'love', 'good morning', 'night', 'sea', 'wine', 'home', 'book']
italian = ['sole', 'amore', 'buongiorno', 'notte', 'mare', 'vino', 'casa', 'libro']

while True:
    # Prompt the user to enter a word for translation
    word = input("Enter a English or Italian word to translate (or press Enter to exit): ").lower()

    if not word:
        break  # Exit the loop if the input is empty

    if word in english:
        # Translate from English to Italian
        index = english.index(word)
        print(f"The Italian translation of '{word}' is '{italian[index]}'.")
    elif word in italian:
        # Translate from Italian to English
        index = italian.index(word)
        print(f"The English translation of '{word}' is '{english[index]}'.")
    else:
        # Word not found, ask if the user wants to add it
        add_word = input("Word not found. Add it to the dictionary? (yes/no): ").lower()
        
        if add_word == "yes":
            language = input("Is the word in English or Italian? ").lower()
            if language == "english":
                translation = input(f"Enter the Italian translation of '{word}': ")
                english.append(word)
                italian.append(translation)
                print(f"'{word}' and its Italian translation '{translation}' added to the dictionary.")
            elif language == "italian":
                translation = input(f"Enter the English translation of '{word}': ")
                italian.append(word)
                english.append(translation)
                print(f"'{word}' and its English translation '{translation}' added to the dictionary.")
            else:
                print("Invalid language choice. Word not added.")
        else:
            print("Word not added to the dictionary.")

