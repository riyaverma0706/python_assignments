'''
Filename: averagerevisited_riya_02.py
Author:   Riya Verma
Purpose:  This program computes the average of the numbers provided .
Revision:
      00: Take the number of values as input to get the average.
      01: Initialize the for loop using the walrus operator and sum function with a range of numbers from the total variable.
      02: Calculate and print the average.
'''
print(" /// Calculate the Average of given number of values. /// \n")
#Step 1: Ask the user for inout of  number of values to get the average.
x = int(input("How many numbers would you like to average?: "))

#Step 2: Initialize the for loop using the walrus operator and sum function with a range of numbers from the total variable.
total = sum((num := float(input(f"Enter a number {i + 1}: "))) for i in range(x)) 

#Step 3: Calculate the average.
average = total / x

#Step 4: Print the result.
print(f"The average is : {average}")                                            
