'''
Program: Language-Trans_Dict_riya_03.py
Author: Riya Verma
Purpose: Program to create an upgraded iteration of language translation utilizing dictionaries 
Revisions:
        00 - Initialized the color dictionary and requested user input for a word"
        01 - Defined while loop for the language translation printing a message if the word isn't found
        02 - Finalized language translation by improving the program and appending words to the current dictionary
'''


#Program Name
print('Program to create an upgraded iteration of language translation utilizing dictionaries  \n')

def rotate_word(word):
    while word[0] != word[1]:
        word.append(word.pop(0))
    return word

#Created a dictionary for colors and stored their respective values
translations = {
    'red':{'french':'rouge','spanish':'rojo','german':'rot','italian':'rossa'},
    'green':{'french':'vert','spanish':'verde','german':'grun', 'italian':'verde'},
    'yellow':{'french':'jaune','spanish':'amarillo','german':'gelb','italian':'gialla'},
    'blue':{'french':'bleu','spanish':'azul','german':'blau','italian':'blu'}
}

print('Available English color Words are : ',end='')
for color in translations:
    print(color+',',end=' ')

#Asking user to enter a input
while True:
    color_input = input('\nPlease Enter a Color in English (or press Enter to quit): ').lower()

    #If the user inputs an empty string, the loop terminates, and the program exits.
    if color_input == '':
        break
      
    if color_input.lower() in translations:
        print("\nAvailable language translations are: german, french, spanish and italian \n")
        # Prompt the user to enter a language
        language_input = input('Please enter a language : ')

        # If the word is in the list, the program prints the translation
        if color_input in translations and language_input in translations[color_input]:
            translated = translations[color_input][language_input]
            print(f"The translation of '{color_input}' in {language_input} is '{translated}'.")
        else:
            print("Sorry, the translation could not be found.")
            add_translation = input(f'\nWould you like to add translation to {color_input} in {language_input} to the dictionary yes <y> or no <n> ')
            if add_translation.lower() == 'y':
                new_translation = input(f'\nPlease enter the translation for {color_input} in {language_input} ')
                translations[color_input.lower()][language_input.lower()] = new_translation.lower()
    else:
        # If the user enters 'y' the word added to the dictionary
        print(f'\nThe word was not found in translations dictionary')
        add_word = input(f'\nDo you like to add translation to {color_input} to the dictionary yes <y> or no <n> ')
        if add_word.lower() == 'y':
            language_addition = input(f'\nWhich language would you like to add for {color_input} ')
            translation_input = input(f'\nPlease enter the translation for {color_input} in {language_addition} ')
            translations[color_input.lower()] = {}
            translations[color_input.lower()][language_addition.lower()] = translation_input.lower()

    print('\nAvailable English color Words are : ',end='')
    for color in translations:
        print(color+',',end=' ')

print('Thank you')
