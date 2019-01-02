#! /usr/bin/env python3
print('Content-type: text/html\n')

import MySQLdb

string = "i211s18_asill"
password = "my+sql=i211s18_asill"

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

html = """ <!doctype html>
        <html>
            <head><meta charset="utf-8">
            <body>
                <h1>Your Tunes Shop</h1>
                <table border='1' width='80%'>
                    <tr><th>SongID</th><th>Song</th><th>Artist</th><th>Genre</th><th>Price</th><th>&nbsp;</th></tr>
                    {0}
                </table>
            </body>
        </html>"""

try:
    SQL1 = "SELECT * FROM Songs;"
    cursor.execute(SQL)
    results = cursor.fetchall()

except Exception as e:
    print("<p>Something went wrong!</p>")
    print(SQL1, "Error:", e)

else:
    table = ""
    for result in results:
        table += "<tr>"
        for item in result:
            table += "<td>" + str(item) + "</td>"
        table += '<td><a href="Purchase.cgi?sid='
        table += str(result[0])
        table += '">Buy</a></td></tr>'

print(html.format(table))
