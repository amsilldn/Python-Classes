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

html = """<!doctype html>
        <html>
        <head><meta charset="utf-8">
        <body>
        <h1>My Tunes</h1>
        <table border='1' width='80%'>
        <tr><th>songID</th><th>Song</th><th>Artist</th><th>Genre</th></tr>
        {content}
        </table>
        </body>
        </html>"""

table = ""

order = form.getfirst("sort")
o = str(order)

try:
    SQL = "SELECT songID, Song, Artist, Genre FROM Songs ORDER BY "+o+";"
    cursor.execute(SQL)
    results = cursor.fetchone()

except Exception as e:
	print("<p>Something went wrong!</p>")
	print(SQL, "Error:", e)

else:
    while results:
        table += "<tr>"
        for result in results:
            table += "<td align='center'>" + str(result) + "</td>"
        table += "</tr>"
        results = cursor.fetchone()


print(html.format(content=table))
