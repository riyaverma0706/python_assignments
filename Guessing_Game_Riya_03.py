
'''
Filename: Guessing_Game_Riya_03.py
Author:   Riya Veram
Purpose:  The objective is to guess a number inside a range in the fewest possible guesses.
Revision:
      00: Importing random and math module
      01: Calculating the number of guesses using the math module and the secret number using the random module.
      02: Use For loop to guess the number.  
'''
# import math and random module
import random
import math

# Take input from user to decide the range
# Use math module for number of guesses
# Use random module To generate the hidden random number within the range.
nMax = int(input("Enter the maximum number in the range: "))
nGuesses = int(math.log2(nMax)) + 1
secretNumber = random.randrange(1, nMax+1)

print(f"Try to guess a secret number from 1 to {nMax} (inclusive).")
print(f"You have {nGuesses} guesses available.")

# Utilize a For loop that iterates through the amount of guesses until it reaches 1.
# If the user correctly predicted the number, the loop is ended, and a success message is shown.
# In case of user runs out of guesses, A failure message and the right secret number are shown
for guessCount in range(nGuesses, 0, -1):
    guess = int(input("Enter your guess: "))

    if guess == secretNumber:
        print("Correct. Well done!")
        break
    elif guess < secretNumber:
        print("The secret number is greater than", guess)
    else:
        print("The secret number is less than", guess)

    if guessCount - 1 > 0:
        print(f"You have {guessCount - 1} guesses available.")
    else:
        print("Sorry. No more guesses are allowed.")
        print("The secret number was", secretNumber)
