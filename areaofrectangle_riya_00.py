'''Author: Riya Verma
... Filename: areaofrectangle_riya_00.py
... Purpose: Compute the area of rectangle
... Revisions :
...     00: Announce and get the input from user for height and width
...     01: Compute the are of rectangle
...     02: print the result
...'''
print('///Compute the area of rectangle ///\n')
# Step 1: Get input for height and width of rectangle
height = float(input("Enter the height of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
# Step 2: Compute the area of rectangle
area = height * width
# Step 3: Display the result
print(f"The area of a {height} by {width} rectangle is {area}.")
