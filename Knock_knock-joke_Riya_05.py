'''
Filename: Knock_knock_joke_Riya_05.py
Purpose: This program generates the knock knock jokes. 
Author: Riya Verma
Revisions:
            00: Importing random function for shuffle.
            01: Defining prompt function for user string to be without punctuation, quotes, uppercase.
            02: Creating a list of knock-knock jokes.
            03: Creating jokes which holds prompt and punchline and shuffling the jokes.
'''
# Importing import random function
import random  

#Defining prompt function for user string to be without punctuation, quotes, uppercase
def validate_prompt_response(prompt_response, accepted_list):
    # remove punctuation
    prompt_response = prompt_response.strip(".?! ")
    # replace quotes
    prompt_response = prompt_response.replace("'", "")
    # lowercase
    prompt_response = prompt_response.lower()
    return prompt_response in accepted_list
    
def validate_joke_response(joke_response, joke):
    joke_response = joke_response.lower()
    joke_response = joke_response.strip(".?! ")
    
    if joke_response == joke.lower() + ' who':
        return True
    else:
        return False

def joke_prompt(joke):
    print('Computer: ' + joke[0])
    joke_response = input('User: ')
    while not validate_joke_response(joke_response, joke[0]):
        print('Incorrect response, please enter: ' + joke[0] + ' who')
        joke_response = input('User: ')
    print('Computer: ' + joke[1])


# Creating a list of knock-knock jokes and define the knock-knock jokes function.
def KnockKnockJokes(number, accepted_list, jokes_list):
    # Acceptable responses from the users.
    print('**********************')
    print('Computer: Knock knock.')  
    # A random joke is produced by code using the jokes_sack list.
    # Accepts the user's response, converts it to lowercase.
    prompt_response = input('User: ')
    
    while not validate_prompt_response(prompt_response, accepted_list):
        print("Incorrect input, please enter: Who's there?")
        prompt_response = input('User: ')

    joke_prompt(jokes_list[number])
    

print("Program for Knock-knock!") 
try:
    accepted_list = ['whos there', 'who is there', 'who there']
    # creating jokes which holds prompt and punchline.
    jokes_list = [('Ice cream', 'Ice cream so you can hear me!'),
                  ('Canoe', 'Canoe come out now?'),
                  ('Avenue', 'Avenue knocked on this door before?'),
                  ('Water', 'Water you asking so many questions for, just open up!'),
                  ('Ears', 'Ears another knock knock joke for ya!')]
    # shuffle the jokes
    random.shuffle(jokes_list)
    
    joke_count = int(input("How many jokes to tell? (Maximum 5) "))
    if joke_count > 5:
        print("Please enter value <= 5")
    else:
        for number in range(0, joke_count):
            KnockKnockJokes(number, accepted_list, jokes_list)
except:
    print("Oops Sorry, please enter the value in numerical form")
