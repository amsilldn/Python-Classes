#! /usr/bin/env python3
print('Content-type: text/html\n')

import MySQLdb, cgi

import cgitb
cgitb.enable()

string = "i211s18_asill"
password = "my+sql=i211s18_asill"

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

form = cgi.FieldStorage()
sid = form.getfirst("sid", "0")

html = """<!DOCTYPE html><html>
        <head><meta charset="utf-8">
        <title>Song Purchased</title>
        </head>
        <body>
        Thanks for purchasing {a}'s' {s} for ${p}
        <form action="ViewSongs.cgi" method="post">
        <h2>View My Songs by</h2>
        <input type="radio" name="sort" value="Song">Title
        <input type="radio" name="sort" value="Artist">Artist
        <input type="radio" name="sort" value="Genre">Genre
        <p>
        <button type="submit">View Songs</button>
        </p>
        </form>
        </body>
        </html>"""

try:
    SQL = "INSERT INTO MyTunes (SongID) Values (" + sid + ");"
    cursor.execute(SQL)
    db_con.commit()

except Exception as e:
	print("<p>Something went wrong!</p>")
	print(SQL, "Error:", e)

else:
    pass

try:
    SQL = "SELECT * FROM Songs Where SongID = " + sid + ";"
    cursor.execute(SQL)
    results = cursor.fetchone()

except Exception as e:
	print("<p>Something went wrong!</p>")
	print(SQL, "Error:", e)

else:
    song = results[1]
    artist = results[2]
    price = results[4]

print(html.format(a = artist, s = song, p = price))
