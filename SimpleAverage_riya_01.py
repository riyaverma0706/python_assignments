'''
Filename: SimpleAverage_riya_01.py
Author:   Riya Verma
Purpose:  This program compute average of the numbers by using for loop.
Revision:
      00: Use of the for loop and range function.
'''


# Ask the user for the input of number of values to average
n = int(input("How many numbers would you like to average? "))

# Initialize variables
total = 0

# Use for loop with the range function 
for i in range(n):
    num = float(input(f"Enter number {i + 1}: "))
    total += num

# Calculate and print the average
average = total / n
print(f"The average is : {average}")
