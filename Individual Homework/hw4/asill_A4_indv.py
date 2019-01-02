#Amanda Sill
#Homework 4
#Group 6

"""
Instructions:
    1.Answer the question: where can you find the Standard Documentation for Python?
    2.Write an algorithm for step 3.
    3.Write a program that asks the user for a path to a directory, then updates the names of all the files in the directory that contain the word draft to instead say final
        EX: "term paper (draft).txt" would be renamed "term paper (final).txt"

BONUS (5pts): for any .txt file that your program changes the name of, have your program add a line of text that states "Edited on " followed by the current date to the end of the text in the file that it is editing.
"""

#1
#https://docs.python.org/3/index.html

#2
#import os & datetime
#define function
    #ask for input
    #if input is a directory
    #loop over directory:
        #create new file variable and tell it to replace the words
        #tell os to rename them
        #update file with edit information

#3
import os
import datetime
def change_name():
    """A function which changes file names and updates them"""

    path = input("Enter a path for a directory: ")
    os.chdir(path)
    files = os.listdir(path)

    try:
        if os.path.isdir(path):
            for file in files:
##              os.rename(file, file.replace("draft", "final"))
                new_file = file.replace("draft", "final")
                os.rename(file, new_file)

                with open(new_file, "a") as item:
                    item.write("\nEdited on ")
                    item.write(str(datetime.datetime.today()))

    except FileNotFoundError:
        print("That is not a valid path. Try again.")
        change_name()

    except Exception:
        print("That is not a valid path. Try again.")
        change_name()

#main
change_name()
