'''
    File name : lottery_game_riya_02.py
    Author    : Riya Verma
    Purpose   : Utilizing 'Powerball Lottery' data, this program generates random lottery predictions.
'''
print (" *** Lottery Guessing Game *** \n")

# Import numpy, pandas and random import numpy as np

import pandas as pd
import random

data_frame pd.read_csv("Lottery_Powerball_Winning_Numbers_.csv")

# Read the CSV file
winning_numbers = np.array(data_frame['Winning Numbers'].values)

# Extract the main numbers and Powerball numbers
all_main_numbers = np.array([list(map(int, item.split()[:5])) for item in winning_numbers])
powerball_numbers = np.array([int(item.split()[-1]) for item in winning_numbers])

# Create sets of unique winning numbers and Powerball numbers
unique_main_numbers = set(all_main_numbers.flatten())
unique_powerball_numbers = set(powerball_numbers.flatten())

# Convert sets to lists
main_numbers_list = list(unique_main_numbers)
powerball_numbers_list = list(unique_powerball_numbers)

# Use random to select 5 numbers from the set of unique winning numbers
predicted_main_numbers = random.sample(main_numbers_list, 5)

# Use random to select 1 number from the set of unique Powerball numbers
predicted_powerball_number = random.sample(powerball_numbers_list, 1)[0]

# Display the predicted next lottery result
print(f"The predicted next lottery result includes the numbers: {predicted_main_numbers} and Powerball number: {predicted_powerball_number}")
