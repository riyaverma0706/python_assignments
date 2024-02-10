'''
Filename: LetterGrade_riyaverma.py
Author:   Riya Verma
Purpose:  To Compute  the final  grades for students based on percentage  using a function.. 
Revision:
      00: Compute the final grades of student based on their percentage.
'''

# Create a function name letterGrade which has a parameter score
def letterGrade(score):

# By using if-elif loop to decide which letter grade to return.  
  if score >= 95:
    return "A+"
  elif score >= 90 and score < 95:
    return "A"
  elif score >= 85 and score < 90:
    return "A-"
  elif  score >= 80 and score < 85:
    return "B+"
  elif  score >= 75 and score < 80:
    return "B"
  elif  score >= 70 and score < 75:
    return "B-"
  elif  score >= 65 and score < 70:
    return "C+"
  elif  score >= 60 and score < 65:
    return "C"
  elif  score >= 55 and score < 60:
    return "C-"
  elif  score < 55:
    return "F"


# Now, the user will have enter a numeric score and that'll be saved variable called 'score'
score = float(input("Enter the numerical score: "))

# Calling the function letterGrade and print the result
grade = letterGrade(score)
print("The letter grade for",score,"percent is", letterGrade(score), " ")
  
