#Amanda Sill
#Team 06

"""
Instructions:
Given a file like this: teams.txtPreview the document

Bears 4

Sharks 7

Cats 9

Hedgehogs 6

Ants 2

Aardvarks 11

Your program should produce output like this:

>>>

The Bears have won 4 games

The Sharks have won 7 games

The Cats have won 9 games

The Hedgehogs have won 6 games

The Ants have won 2 games

The Aardvarks have won 11 games

Teams with names shorter than 5 letters: ['Cats', 'Ants']

The three teams with the highest wins are: ['Aardvarks', 'Cats', 'Sharks']

Your mission will be to do the following:
    1.Develop an algorithm to solve all remaining steps in this problem.
    2.Use a list comprehension to load the data from a file named “teams.txt”. There’s a sample filePreview the document on Canvas with the data shown above.
    3.Print out the information read in from the file formatted as shown in the example.
    4.Use a list comprehension to create a list of the names of teams with less than 5 letters in their name.
    5.Use a list comprehension to create a list of the names of the three teams with the highest wins.
"""

#1 Develop an algorithm to solve all remaining steps in this problem.
#open file using list comprehension
#loop through items of list and print out team names and # of games won
#loop through list of lists
    #if item[0] has a length < 5
        #add to list using list comprehension
#loop through list of lists
    #for 3 item[i]s with the highest scores
        #add them to the list using list comprehensions

#2 Use a list comprehension to load the data from a file
file_contents = [line.strip().split(" ") for line in open("teams.txt", "r")]
print(file_contents)

#3 Print out the information read in from the file
for item in file_contents:
    print("The", item[0], "have won", item[1], "games")

#4 Use a list comprehension to create a list of the names of teams with less
    #than 5 letters in their name.
less = [item[0] for item in file_contents if len(item[0]) < 5]
print("Teams with names shorter than 5 letters: ", less)

#5 Use a list comprehension to create a list of the names of the three teams
    #with the highest wins.

#this one prints the correct answer but not in the correct order and would
#only work for this list
scores = [item[0] for item in file_contents if int(item[1]) >= 7]
print("The three teams with the highest number of wins are: ", scores)

#this one somehow can't tell that 11 is the highest number?
#it also does not print them in descending order
##wins = [item[0] for item in sorted(file_contents, reverse = True)[:3]]
##print("The three teams with the highest number of wins are: ", wins)


##t = [max(i) for item in file_contents for i in range(3)]
##print(t)
