#Amanda Sill
#asill
#Group 06
#Homework 7

import xml.etree.ElementTree as et, datetime
#1
'''Write a function called display_book that prints the title,
author, and price of the book with a certain id (passed as a
parameter). Example call: display_book(“bk107”)'''
#import things
#define function with parameter
#set root
#look under book heading
#print description

def display_book(book_id):
    root = et.parse("library.xml")
    books = root.iter("book")

    print("The title, author, and price of that book is: ")
    
    for book in books:
        if book_id == book.attrib['id']:
            print("Title: ", book.find("title").text, "\nAuthor: ", book.find("author").text,
                  "\nPrice: $", book.find("price").text)

#main
display_book("bk107")

#2
'''Display the title, author, and price of each Computer book
released in December.'''
#parse file
#look under at book heading
#print description
#iterate through book children
    #if the genre is computer and it was released in december
        #print the title, author, and price

root = et.parse("library.xml")
books = root.iter("book")

print("\nThe Computer books released in December are: ")
for book in books:
    if book.find("genre").text == "Computer" and "12" in book.find("publish_date").text:
        print("Title: ", book.find("title").text, "\nAuthor: ",
              book.find("author").text, "\nPrice: $", book.find("price").text, "\n")


#3
'''Print all the genres in the file.'''
#use parse and book stuff from number 2
#use findall to generate list of the genre listed of ever book in file
#create new empty list for genres
#loop through findall list
    #if the genre is not already in the second list
        #add to second list
#loop through second list
    #print each item

genres = root.findall("book/genre")
genre_list = []

for genre in genres:
    if genre.text not in genre_list:
        genre_list.append(genre.text)

print("The genres are: ")
        
for genre in genre_list:
    print(genre)
