'''
Filename: Cypher_riya_01.py
Author:   Riya Verma
Purpose:  Convert a user-entered word into a numeric code based on an encryption scheme.
Revision:
      00: Request input from the user and lowercase it.
      01: Iterates through word's individual letters.
      
'''

# Ask the user for a word
word = input("Enter a word: ")

# Converting the word to lowercase
word = word.lower()

# Store list in numeric code
numeric_code = []

# Iterate through word's individual letters
for letter in word:
    if 'a' <= letter <= 'z':
        # Calculate the numeric code for the letter
        numeric_code.append(ord(letter) - ord('a'))

# Print the numeric code for the word
print("The numric code for word",word, "is:", ", ".join(map(str, numeric_code)))
