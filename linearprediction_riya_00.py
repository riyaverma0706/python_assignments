'''Author: Riya Verma
... Filename: linearprediction_riya_00.py
... Purpose: Predict the next number in Linear sequence
... Revisions :
...     00: Announce and get the first and second number of the sequence
...     01: Compute the common difference
...     02: predict and print the result
... '''
print('///Predict the next number of the linear sequence ///\n')
# Step 1: Get input for the first and second number of the linear sequence
first_number = int(input("Enter the first integer: "))
first_number = int(input("Enter the first integer: "))
#Step 2: Compute the common difference
common_diff = second_number - first_number
#Step 3: predict and print the result
next_number = second_number + common_diff
print(f"The next number in the linear sequence is {next_number}.")
