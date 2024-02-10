'''
Filename: super_scramble_riya_05.py
Author:   Riya Verma
Purpose:  This program creates six seven letter  words from a scrambled list of characters.
Revision:
      00: Creating List.
      01: Defining rotate function and placing integer value at 0 position.
      02: Rotating list without changing the the order of the characters
      03: Sorting the tuples based on the integer value in each using lambda function.
      04: Using join() method to join the characters to form strings
      05: Print the result
'''

#Creating List
mess = [['o', 'c', 'h', 'c', 'a', 64, 'd'],
        ['o', 'o', 91, 'y', 'y', 'e', 'i'],
        ['u', 'r', 'o', 'u', 'y', 46, 'e'],
        ['u', 'y', 'e', 'r', 19, 't', 't'],
        ['a', 'h', 55, 's', 'n', 'i', 's'],
        [27, 'u', 'r', 't', 'r', 'r', 'n'],
        [72, 'a', 'c', 'p', 't', 'g', 'm']]

#Program Name
print('Super scramble challenge - Program to discover six seven letter words \n')

#Defining rotate function and placing integer value at 0 position
def rotate(lst):
    while type(lst[0]) != int:
        lst.insert(0, lst.pop())
    return lst
    
#Rotating list without changing order of characters
z = [rotate(i) for i in  mess]

#Sorting the tuples based on the integer value in each using lambda function
words = []
for i in range(len(z[0])-1):
    sorted_z = sorted(z,key = lambda a:a[i])
    word = [a[i+1] for a in sorted_z]
    #Using join() method to join the characters to form strings
    words.append(''.join(word))

#Printing the result
print("\n".join("".join(i) for i in words)) 
