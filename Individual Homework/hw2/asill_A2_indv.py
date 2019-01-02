#Amanda Sill
#asill
#group 6
#indv hw 2

"""
Instructions:
1. Write a program that implements the word guessing game (hangman) we wrote an algorithm for in Lecture 2 (you may use the algorithm provided in that lecture to help you write your code).

2. Write a program to implement a rock paper scissors game using your algorithm from HW 1.
"""

#1 - hangman
#I tried the algorithm provided in class and hated it. I like mine better.
#imports
from random import *
#create win lose vaiables
wins = 0
losses = 0

#create function and have it take variables
def hangman(wins, losses):
    #create game variable and set to true
    game = True

    #welcome and intro
    print("Welcome to Hangman!")

    #loop de loop
    while game:
        #create list of words - these are all real words. feel free to google.
        comp = ["xiphoid", "dizzying", "verisimilitude", "xylem", "euouae", "triphthong",
                "voyeurism", "iatrogenic", "giaour", "phlem", "quixotic", "kerfuffle",
                "naphtha", "larynx", "syzygy", "axolotl", "quinoa", "buxom", "axiom"]
        #define secret word
        word = choice(comp)
        #create a revealed letter list that starts empty
        reveal_lst = []
        #create guessed letters list
        guessed_let = []
        #set wrong guess count to 0
        wrong = 0

        #for every letter in the word
        for letter in word:
            #put a dash in the revealed letter list
            reveal_lst.append("_")

        #loop again
        while wrong < 10:
            #join letters in guessed list
            joined = "".join(reveal_lst)
            print(joined  + "\n")

            #user input
            user = input("Please guess a letter: ")
            guessed_let.append(user)
            join1 = "".join(guessed_let)
            #print("Guessed letters:", join1)

            #go through the word
            for i in range(len(word)):
                #if the user letter is in the word
                if user == word[i]:
                    #add to the reveal list
                    reveal_lst[i] = user

            #if user input not in the word
            if user not in word:
                #update count & tell user they were wrong
                wrong += 1
                print("That guess was incorrect.")

            #tell the user the letters they guessed
            print("Guessed letters:", join1)

            #if no more _ in reveal list
            if "_" not in reveal_lst:
                #tell the user they won
                print("\nYou won! The word is", word + "!")
                wins += 1
                break

            #if count is 10
            if wrong == 10:
                #tell user they lost and break loop
                print("\nYou lost. The word is", word + "!")
                losses += 1
                break

        print("\nWins: ", wins, "and Losses: ", losses)

        #ask if the user wants to play again
        again = input("Would you like to play again? ")

        #if the user doesn't want to play again
        if again.upper() != "YES":
            #update game to false
            game = False
            print("\nOk. Goodbye.")

#main
#call the function
hangman(wins, losses)

#--------------------------------------------------------------------------------------
#2 - rock paper scissors
#I don't know how ok the rubric is with 2 functions, but here you go.
#import modules
import random
#optional variables for counting number of wins and losses
wins = 0
losses = 0

#looping of game
#create second function which takes 2 variables (similar to the optional variables)
def loop(wins, losses):
    """a function which loops the game"""

    #print number of wins and losses and ask if user wants to play again
    print("Wins:", str(wins), "\nLosses:", str(losses))
    #create variable for user input
    user_ques = input("Do you want to play again? ")

    #if the user says yes
    if user_ques.upper() == "YES":
        #run the first game function
        game(wins, losses)
    elif user_ques.upper() == "NO":
        print("Thanks for playing! \nGoodbye.")


#create a function for the game (will take won/loss variables if included)
def game(wins, losses):
    """a function which creates the rock paper scissors game"""

    #print stuff to let the user know what is going on (i.e. game name)
    print("Rock Paper Scossors")
    #create user choice variable using input
    user_choice = input("Choose Rock, Paper, or Scissors: ")
    #create computer choice variable using random
    comp_choice = random.randint(0,2) #I could make a list and have the computer choose
                                        #from that, but that feels like more work

    #if the user chooses rock
    if user_choice.upper() == "ROCK":
        #if the computer chooses rock/0
        if comp_choice == 0:
            #print draw and end game (update optional variables)
            print("Its a draw.")
            loop(wins, losses)
        #if the computer chooses paper/1
        elif comp_choice == 1:
            #print you lost and end game (update optional variables)
            losses += 1
            print("Paper beats Rock. You lost.")
            loop(wins, losses)
        #if the computer chooses scissors/2
        elif comp_choice == 2:
            #print you won and end game (update optional variables)
            wins += 1
            print("Rock beats Scissors. You won.")
            loop(wins, losses)

    #if the user chooses paper
    if user_choice.upper() == "PAPER":
        #if the computer chooses rock/0
        if comp_choice == 0:
            #print you won and end game (update optional variables)
            wins += 1
            print("Paper beats Rock. You won.")
            loop(wins, losses)
        #if the computer chooses paper/1
        elif comp_choice == 1:
            #print draw and end game (update optional variables)
            print("Its a draw.")
            loop(wins, losses)
        #if the computer chooses scissors/2
        elif comp_choice == 2:
            #print you lost and end game (update optional variables)
            losses += 1
            print("Scissors beats Paper. You lost.")
            loop(wins, losses)

    #if the user chooses scissors
    if user_choice.upper() == "SCISSORS":
        #if the computer chooses rock/0
        if comp_choice == 0:
            #print you lost and end game (update optional variables)
            losses += 1
            print("Rock beats Scissors. You lost.")
            loop(wins, losses)
        #if the computer chooses paper/1
        elif comp_choice == 1:
            #print you won and end game (update optional variables)
            wins += 1
            print("Scissors beats Paper. You won.")
            loop(wins, losses)
        #if the computer chooses scissors/2
        elif comp_choice == 2:
            #print draw and end game (update optional variables)
            print("Its a draw.")
            loop(wins, losses)

#main
#ask the user if he/she wants to play rock paper scissors
user_in = input("Do you want to play Rock Paper Scissors? ")

#if user says yes
if user_in.upper() == "YES":
    #run first game function
    game(wins, losses)
elif user_in.upper() == "NO":
    print("OK. Goodbye.")
