'''
Program_Name: send_more_money_puzzle
Filename: send_more_money_riya_05.py
Author:  Riya Verma
Purpose: To solve the Send more more Puzzle - Assigning interger values can be substituted to make the addition correct.
Revisions:
        00 - Importing permutations to create digit permutations.
        01 - Defining Function and Permutating the digits 0 to 9 in 8 position
        02 - Assigning the generated permutation of digits to the letters
        03 - Validating the assignment by ensuring no leading zeros and correct equation
        04 - Returning vales and printing the result
'''

print("***   SEND MORE MONEY PUZZLE  *** \n")

#This program uses itertools permutations to create digit permutations
from itertools import permutations

#Function definition
def smm_puzzle():
    
    #Permutating the digits 0 to 9 in 8 positions
    for p in permutations(range(10), 8):
        
        #Assigns the generated permutation of digits to the letters S, E, N, D, M, O, R, and Y.
        s, e, n, d, m, o, r, y = p

        #Validating assignment by ensuring no leading zeros and correct equation
        if s != 0 and m != 0 and (1000*s + 100*e + 10*n + d) + (1000*m + 100*o + 10*r + e) == (10000*m + 1000*o + 100*n + 10*e + y):
            
            #Returns values
            return ({'S': s, 'E': e, 'N': n, 'D': d, 'M': m, 'O': o, 'R': r, 'Y': y})


#Calling the Function and Printing the result
result = smm_puzzle()
print(result)
