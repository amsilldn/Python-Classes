import xml.etree.ElementTree as et, datetime

root = et.parse("library.xml")
books = root.iter("book")

print("The Computer books released in December are: ")
for book in books:
    if book.find("genre").text == "Computer" and "12" in book.find("publish_date").text:
        print("Title: ", book.find("title").text, "\nAuthor: ",
              book.find("author").text, "\nPrice: $", book.find("price").text)
