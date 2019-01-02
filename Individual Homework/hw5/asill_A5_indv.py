#Amanda Sill
#Indv homework 5
#Group 6

"""
Instructions:
    1.Answer the question: when using strftime what is the placeholder that will display the full name of the day of the week (Monday, Tuesday, etc.). (ex. "%d" is the placeholder that displays the day as a two digit number)

    2.Write an algorithm for step 3.

    3.Write a program that reads in the information from a file called ShopRecords.csvPreview the document and displays all of the items that were sold on a weekend.
"""

#1
# %A

#2 & 3
#Write a program that reads in the information from a
#file called ShopRecords.csv and displays all of the
#items that were sold on a weekend.

#import
#define function
#open file
#create empty list
#loop through file
    #split date on /
    #give date formatting  with datetime in a variable
    #if the items were sold on a saturday or sunday
        #add items to list
#loop through list
    #print items
#call function in main

import csv
import datetime

def weekend():
    """a function which looks through ShopRecords.csv and prints out items sold on weekends"""

    file = csv.DictReader(open("ShopRecords.csv", "r"))

    weekend_lst = []

    #this would suck to do as a list comprehension - were we supposed to do that?
    for entry in file: #look at all the things
        month, day, year = entry["Date"].split("/") #don't want that slash
        sold = datetime.date(int(year), int(month), int(day)) #formatting, formatting, formatting

        if sold.strftime("%A") == "Saturday" or sold.strftime("%A") == "Sunday": #%A comes back around
            weekend_lst.append(entry["Item"])

    for item in weekend_lst: #for printing each item on a new line
        print(item, "\n")

#main
weekend()

#alternatively, if you wanted it to work for any csv file with the same headings...

#import
#define function which takes a file
#open file
#create empty list
#loop through file
    #split date on /
    #give date formatting  with datetime in a variable
    #if the items were sold on a saturday or sunday
        #add items to list
#loop through list
    #print items
#ask user to input a csv file name
#call function w/ user input in main

def weekend1(file):
    """a function which takes a csv file input from the user,
        loos through the file, and prints out items sold on weekends"""

    data = csv.DictReader(open(file, "r"))

    weekend_lst = []

    for entry in data:
        month, day, year = entry["Date"].split("/")
        sold = datetime.date(int(year), int(month), int(day))

        if sold.strftime("%A") == "Saturday" or sold.strftime("%A") == "Sunday":
            weekend_lst.append(entry["Item"])

    for item in weekend_lst:
        print(item, "\n")

#main
##userCSV = input("Please enter a csv file name: ")
##
##weekend1(userCSV)
