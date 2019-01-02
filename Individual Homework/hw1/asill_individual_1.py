#Amanda Sill
#asill
#team 6 (I think?)
#HW 1

"""
Instructions:
    1.You must complete the Academic Integrity and Syllabus quiz in the Tests & Surveys section of Canvas with a 100% score (you may retake the quiz as many times as needed) You will receive a 0 on this assignment if you have not completed the quiz by the time the assignment is due.

    2.Write an algorithm for a Rock Paper Scissors game. The user should enter either rock, or paper, or scissors while the computer makes its choice randomly. The two choices are then compared with the user being told whether they won, lost, or tied. For this game Rock beats Scissors, which beats Paper, which beats Rock. Include your algorithm as comments in your submission.
    See herePreview the document for an example of what an algorithm should look like.
    If you submit python code instead on an algorithm you will not receive points for this question.

    3.Write a program that ask the user for a string as input. It should reverse the order of all the characters in the string and print it back out to the user. For example: AbC123 would be printed out as 321CbA

    4.Write a program that takes two lists and displays True if they have at least one member in common, False otherwise.
"""

#1 - Syllabus Quiz
#Done

#2 - Algorithm
#import modules
#optional variables for counting number of wins and losses
#create a function for the game (will take won/loss variables if included)
    #print stuff to let the user know what is going on (i.e. game name)
    #create user choice variable using input
    #create computer choice variable using random

    #if the user chooses rock
        #if the computer chooses rock/0
            #print draw and end game (update optional variables)
        #if the computer chooses paper/1
            #print you lost and end game (update optional variables)
        #if the computer chooses scissors/2
            #print you won and end game (update optional variables)

    #if the user chooses paper
        #if the computer chooses rock/0
            #print you won and end game (update optional variables)
        #if the computer chooses paper/1
            #print draw and end game (update optional variables)
        #if the computer chooses scissors/2
            #print you lost and end game (update optional variables)

    #if the user chooses scissors
        #if the computer chooses rock/0
            #print you lost and end game (update optional variables)
        #if the computer chooses paper/1
            #print you won and end game (update optional variables)
        #if the computer chooses scissors/2
            #print draw and end game (update optional variables)

#optional looping of game
#create second function which takes 2 variables (similar to the optional variables)
    #print number of wins and losses and ask if user wants to play again
    #create variable for user input
    #if the user says yes
        #run the first game function

#ask the user if he/she wants to play rock paper scissors
#create user input variable
#if user says yes
    #run first game function

#3 Reverse String
#create program
def reverse_lst():
    """A program which reverses a user-input string"""
    #ask for user to input a string
    user = input("Please enter a string: ")
    #put string into a list
    user_lst = list(user)
    #reverse the list
    rev_lst = user_lst[::-1]
    #convert list back into string
    rev_user = ''.join(rev_lst)
    #return the string
    return rev_user

#main
print(reverse_lst())

#4 Lists
#create function
def compare(x, y):
    """A program that takes two lists and displays True if they
    have at least one member in common, False otherwise."""
    #create a list for comparison
    comp_lst = []
    #loop through the first list
    for item in x:
        #if an item in the second list is in the first list
        if item in y:
            #add item to comparison list
            comp_lst.append(item)
    #if the length of the first list is 0 print false
    if len(comp_lst) == 0:
        print(False)
    #else print true
    else:
        print(True)

#main
lst1 = ["Aspargus", "Broccoli", "Carrots"]
lst2 = ["Potatoes", "Carrots", "Celery"]
compare(lst1, lst2)

lst1 = ["Petunia", "Daisy", "Lilac"]
lst2 = ["Potatoes", "Carrots", "Celery"]
compare(lst1, lst2)
