#Amanda Sill
#asill
#Team 06
#homework 6

"""
Instructions:
    1.Answer the question: what is the Python regular expression pattern that would match a hex color (Links to an external site.)Links to an external site. code. (for example, the pattern that would match an email address is '[\w.-]+@[\w.-]')

    2.Write an algorithm for step 3. As part of your algorithm, be sure to describe the pattern you're using to find the win/loss result for each game.

    3.Write a program that looks at the source of http://cgi.soic.indiana.edu/~dpierz/mbball.html (Links to an external site.)Links to an external site. (a copy of the IU men's basketball team record page). Use regular expressions to find all the games IU has played in this year and calculate the total number of wins and losses (including exhibition games)

     The output should look like the following:

Wins: 18
Losses: 12

Bonus [10 pts]. Extend your code from part 3 to also calculate the total difference in points scored in all the games (a game that finished 68-71 would have a difference of 3 points, 85-52 a difference of 33 points etc)

Total Difference: 431

Remember, as always good coding practices are part of the grade so be sure to comment your code, use good variable names, efficient regular expressions, etc.
"""

#1
'''
#([0-9a-fA-F]{3}){1,2} - does not catch hashtags
OR
#[0-9a-zA-Z]{3}[0-9a-zA-Z]{3} - will also catch hastags
OR
#[\w]{3}{1,2}- will also catch hashtags
'''

#2
#import stuff
#define function
#copy and paste webpage stuff from class python files
#define win and loss variables and set to 0
#use re.findall to pull all the game results from the url
    #pattern: letter space 2 numbers dash 2 numbers
#loop through what was found
#if the first part is W
#add 1 to win
#else if the first part is L
#add 1 to loss
#print scores


#3
#<div class='schedule_game_results'><div>W 93-62</div>
import re, urllib.request, ssl

def iu_games():
    """print wins and losses from iu men's basketball webpage"""
    #webpage stuff
    context = ssl._create_unverified_context()
    web_page = urllib.request.urlopen ("http://cgi.soic.indiana.edu/~dpierz/mbball.html",context=context)
    lines = web_page.read().decode(errors="replace")
    web_page.close()

    #variables
    wins = 0
    losses = 0

    #find all
    all_scores = re.findall("(?<=class='schedule_game_results'><div>)[A-Z][ ][0-9]{2}-[0-9]{2}.*?(?=</div)", lines)

    #loop through list to find the stuff and update variables
    for score in all_scores:
        if score[0] == "W":
            wins += 1
        elif score[0] == "L":
            losses += 1

    #print info
    print("Wins:", wins, "\nLosses:", losses)

#main
#iu_games()

#BONUS
#import stuff
#define function
#copy and paste webpage stuff from class python files
#define win and loss variables and set to 0
#use re.findall to pull all the game results from the url
        #pattern: 2 numbers dash 2 numbers
#loop through what was found
#if the first 2 indexes as an integer are greater than the 4th and 5th indexes
#subtract the first concatenated integer from the second and add to total dif
#add 1 to win
#else if the 4th and 5th indexes and greather than the first two
#subtract the second concatenated integer the first
#add 1 to loss
#print scores and total dif

import re, urllib.request, ssl

def iu_games_calc():
    """calculates total point difference between wins and losses"""
    #webpage stuff
    context = ssl._create_unverified_context()
    web_page = urllib.request.urlopen ("http://cgi.soic.indiana.edu/~dpierz/mbball.html",context=context)
    lines = web_page.read().decode(errors="replace")
    web_page.close()

    #variables
    wins = 0
    losses = 0
    total_dif = 0

    #find all
    all_scores = re.findall("(?<=class='schedule_game_results'><div>[A-Z][ ])[0-9]{2}-[0-9]{2}.*?(?=</div)", lines)

    #loop through the list to find stuff, do math, and update variables
    for score in all_scores:
        if int(score[0]+score[1]) > int(score[3]+score[4]):
            total_dif += int(score[0]+score[1]) - int(score[3]+score[4])
            wins += 1
        elif int(score[0]+score[1]) < int(score[3]+score[4]):
            total_dif += int(score[3]+score[4]) - int(score[0]+score[1])
            losses += 1

    #print info
    print("Wins: ", wins, "\nLosses: ", losses, "\nTotal Difference: ", total_dif)

#main
iu_games_calc()
