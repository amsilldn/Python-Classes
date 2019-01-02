#Amanda Sill
#Lab Practical 2
#Group 6

#import statements
#define function
#copy and paste web stuff from in-class work
#find headlines using re.findall
    #pattern: tag with "headline", all the things, end of tag
#loop through headlines and print them all
#ask user for input
#loop through headlines
    #if user input in in headline
        #print headline

import re, urllib.request, ssl, random, webbrowser, os
#part 1, 2, 3 & BONUS

def news(url):
    print("Searching:", url, "\n")

    #web stuff
    context = ssl._create_unverified_context()
    web_page = urllib.request.urlopen (url,context=context)
    lines = web_page.read().decode(errors="replace")
    web_page.close()

    #bonus attept
    url = re.findall('(?<=itemprop="url" href=").+?(?=</span)', lines, re.DOTALL)

    #headlines
    titles = re.findall('(?<=itemprop="headline">).+?(?=<)', lines)

    #print all titles
##    for title in titles:
##        print(title, "\n")

    #user input
    user = input("Please enter a word to search for: ")

    #print relevant things
    for title in titles:
        if user.lower() in title.lower():
            print("\n", "\t", title, "\n")
            #webbrowser.open_new_tab(url) - NOPE

#main
news("http://cgi.soic.indiana.edu/~dpierz/news.html")


    
