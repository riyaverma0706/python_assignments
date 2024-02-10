'''
Filename: scramble_challenge_riya_02.py
Author:   Riya Verma
Purpose:  This program creates words from a scrambled list of characters
Revision:
      00: Creating List.
      01: Sorting the tuples based on the integer value in each using lambda function.
      03: Creating List of characters using list comprehension.
      02: Using join() method to join the characters to form strings
      03: Print the result
'''
#Program Name
print('Scramble Words \n')

#Creating List.
z = [('v', 'c', 'l', 6, 'r'), ('i', 'a', 'i', 4, 't'),
('a', 'f', 'g', 1, 'p'), ('h', 'n', 'r', 3, 's'),
('e', 'e', 'a', 7, 'e'), ('c', 'i', 'o', 2, 'a'),
('e', 'n', 'l', 5, 'u')]

#Sorting the tuples based on the integer value in each using lambda function.
z = sorted(z, key = lambda x:x[3])

#Creating List of characters using list comprehension.
z = [ [z[x][i] for x in range(len(z)) ] for i in range(len(z[0])) if i != 3 ]

#Using join() method to join the characters to form strings
result = [''.join(words) for words in z]

#Printing the result
print(result)
