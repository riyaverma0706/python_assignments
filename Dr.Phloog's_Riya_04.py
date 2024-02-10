'''
Filename: Dr.Phloog's_Riya_04.py
Program: Dr.Phloogs Class
Author: Riya Verma
Purpose: Program to calculate grades for Dr. Phloog 
Revisions:
           00: Determine how many grades to omit.
           01: Calculate the average after excluding the lowest scores.
           02: Determine the letter grade
'''

# define fineGrade
def findGrade(grades):
    # Determine the number of grades to exclude
    num_grades_to_exclude = len(grades) // 3
    
    # Exclude the lowest grades among all
    grades.sort()
    grades = grades[num_grades_to_exclude:]
    
    # Evaluate the average
    total = sum(grades)
    average = total / len(grades)
    
    # Compute the letter grade
    if average < 80:
        letter_grade = 'X'
    elif average > 90:
        letter_grade = 'Z'
    else:
        letter_grade = 'Y'
    
    return (average, letter_grade)



print('Program to calculate grades for Dr. Phloog\n')
# CODE FOR TESTING THE FUNCTION
grades = []
#grades.append([50,100,60]) # [80.00,'Y']
#grades.append([50,100,50,50,100,50,50,100,50]) # [75.00,'X']
grades.append([65,100,22,89,0,100,92,78,87,97]) # [91.86,'Z']
#grades.append([90,70,60,100,65,95,27,55,79,60]) # [79.86,'X']
#grades.append([65,100,22,89,45,92,78,87]) # [85.17,'Y']
for item in grades:
    grades = findGrade(item)
print(f"{grades[0]:6.2f} --> {grades[1]} ")
