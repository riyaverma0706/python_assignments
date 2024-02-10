'''
Filename: double-scramble_riya_03.py
Author:   Riya Verma
Purpose:  This program creates words from a scrambled list of characters without changing the order of the characters.
Revision:
      00: Creating List.
      01: Defining get_index function - to get index of int value from list.
      02: Rotating list without changing the the order of the characters
      03: Sorting the tuples based on the integer value in each using lambda function.
      04: Creating List of characters using list comprehension.
      05: Using join() method to join the characters to form strings
      06: Print the result
'''
#Program Name
print('Double scramble challenge \n')
      
#Creating List.
z = [['s', 'a', 3, 't', 'n'],['h', 'b', 'c', 1, 'p'],
['h', 'y', 'c', 'k', 5],[4, 'c', 'e', 'i', 'l'],
['o', 'a', 'h', 2, 'i']]


#Defining get_index function - to get index of int value from list
def get_index(l):
    for i in range(len(l)):
        if type(l[i]) == int:
            return i

#Rotating list without changing the the order of the characters
z = [l[get_index(l):] + l[:get_index(l)] for l in z]

#Sorting the tuples and placing intger value at 0 position.
z = sorted(z, key = lambda x:x[0])

#Creating List of characters using list comprehension.
z = [ [z[x][i] for x in range(len(z)) ] for i in range(len(z[0])) if i != 0 ]

#Using join() method to join the characters to form strings
result = [''.join(words) for words in z]

#Printing the result
print(result)

