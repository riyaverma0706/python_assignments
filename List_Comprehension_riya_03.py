'''
Filename: List_Comprehension_riya_03.py
Author: Riya Verma
Simple List Comprehension excercise and Sorting Questions

the list comprehension tasks found here.
Every function you build needs to include:
(1) a documentation string outlining the parameters that are in and the value that is returned; and
(2) a minimum of two important tests that validate the function.
'''


#### Question 1. List comprehension analysis
# Code
def linc(a, b=2):
    ''' use of list comprehension to add b to each element in a'''
    return [x + b for x in a if type(x) == int]


x = [1, 2, 3, 4]
y = linc(x)  # [5,6,7]
z = linc(x,1)  # [3,5,6] print(x) print(y) print(z)
print(x)
print(y)
print(z)


#### Question 2. the listInc() function
def listInc(a):
    '''use of list comprehension to increment each positive element in a'''
    return [x + 1 for x in a]

### listInc() tests
assert listInc([7,2,4,8]) == [8,3,5,9], 'listInc failed [7,2,4,8]'
assert listInc([9,-1,0,5]) == [10,0,1,6], 'listInc failed [9,-1,0,5]'
print('listInc is OK\n')


#### Question 3. the listOut() function
def listOut(a):
    '''this function prints each item in the list on a separate line.'''
    for x in a:
        print(x)

### listOut() tests
listOut([7,2,'OK',8])
print()
listOut([[1,2],2.0,'$',8])
print()


#### Question 4. statements that move items between lists
### end of A to beginning of B
a,b = [1,2,3], [4,5,6]
b.insert(0, a.pop())
print(a,b)


### beginning of A to end of B
a,b = [1,2,3], [4,5,6]
b.append(a.pop(0))
print(a,b,'\n')

#### Question 5a. rotateForward() function
def rotateForward(a):
    '''With the final element of an as the first element and the remaining items of an as the remaining elements, this method returns a new list.'''
    return [a[-1]] + a[:-1]

### rotateForward() tests
assert rotateForward([1,2,3,4]) == [4,1,2,3], 'rotateForward failed'
print('rotateForward ok\n')


#### Question 5b. rotateBackward() function
def rotateBackward(a):
    '''This function yields a new list where the last element is the first element of a and the remaining items are the remaining elements of a.'''
    return a[1:] + [a[0]]

### rotateBackward() tests
assert rotateBackward([1,2,3,4]) == [2,3,4,1,], 'rotateBackward failed'
print('rotateBackward ok\n')


#### Question 6. Analysis of iSort()
def iSort(x,n=2):
    ''' This function returns a list of x that has been sorted according to each tuple's n-th element.'''
    return sorted(x, key=lambda t: t[n])

x = [(1,'one','uno'),(2,'two','dos'),(3,'three','tres')]
print(iSort(x))
print(iSort(x,1))
print()


#### Question 7. Length sorting
z = ['bzz','z','cz','azzz']
z.sort(key=len)
print(z,'\n')


#### Question 8. backSort() function
def backSort(a):
    '''This function creates a sorted list of a by using each string's reverse.'''
    return sorted(a, key=lambda s: s[::-1])

assert backSort(['red','yellow','blue','green','black']) == \
['red', 'blue', 'black', 'green', 'yellow'], 'backSort FAILED'
print('backSort OK')
