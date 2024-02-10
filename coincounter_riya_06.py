'''
Filename: coincounter_riya_06.py
Author:   Riya Verma
Purpose:  This program calculates the total amount of the coins given as an input string.
Revision:
       01- Obtain the user's input string for the different coin types.
       02- Define dictionaries to record the details of each coin.
       03- Count the number of each type of coin given in the input string.
       04- The input string asks user to count how many of each kind of coin is there.
       05- Format the coin counter report and print it.
'''
print(" /// Program to count coins and calculate values /// \n")

#Step 1: Get the input string from the user
coin_string = input("Enter the string of coins (p: Penny, n: Nickel, d: Dime, q: Quarter, h: Half-Dollar): ")

#Step 2: Define names and values of coins in a dictionary.
coin_values = {'p': 0.01, 'n': 0.05, 'd': 0.10, 'q': 0.25, 'h': 0.50}
coin_names = {'p': 'Penny', 'n': 'Nickel', 'd': 'Dime', 'q': 'Quarter', 'h': 'Half-Dollar'}

#Step 3: Initialize dictionaries to store counts and values of each coin.
coin_counts = {}
coin_total_values = {}

#Step 4: Iterate each character in the input string one by one.
for char in coin_string:
    if char in coin_values:
        coin_counts[char] = coin_counts.get(char, 0) + 1
        coin_total_values[char] = coin_total_values.get(char, 0) + coin_values[char]

#Step 5: Calculate the total money value.
total_value = sum(coin_total_values.values())

#Step 6: Print the header of report.
print("===================")
print("Coin Counter Report")
print("===================")
print("Coin         Count      Value")
print("==============================")

#Step 7: Iterate the coin types and print the result.
for coin_type, coin_value in coin_values.items():
    if coin_type in coin_counts:
        coin_count = coin_counts[coin_type]
        coin_name = coin_names[coin_type]
        coin_total = coin_total_values[coin_type]
        print(f"{coin_name:<10}: {coin_count} coin(s) = ${coin_total:.2f}")

#Step 8: Print the total amount of money.
print("\nTotal amount: $" + f"{total_value:.2f}")
