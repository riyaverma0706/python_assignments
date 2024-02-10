'''
Filename: TextGraph_riya_02.py
Author: Riya Verma
Purpose: This program generates a bar graph as per the numbers entered.
Revision:
    00 - Divides the user's input into distinct numbers depending on spaces.
    01 - isdigit method to check the imput is in digit or not
    02 - if input is valid and correct, it print bar garph using "="
    03 - Printing a bar graph based on inputted data
'''
# Announcement on the next line
print("TextGraph: Draw a bar graph using text")
#Ask user to provide input
response = input("Enter up to 5 positive integers less than 50: ")

#isdigit method to check the imput is in digit or not
numbers=response.split()
valid_numbers_count = 0
#Applying for loop to print graph for the digits entered
for n in numbers:
  if valid_numbers_count >= 5:
    break
  if n.isdigit():
      num = int(n)  
      if 0 < num < 50:
          graph=int(n)*'='
          print(graph)
      else:
            print('?')
  else:
        print('?')
