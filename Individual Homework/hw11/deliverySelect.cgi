#! /usr/bin/env python3

print('Content-type: text/html\n')

import MySQLdb, cgi, cgitb

string = "i211s18_asill"
password = "my+sql=i211s18_asill"

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

cgitb.enable()

form = cgi.FieldStorage()

html = """
<!doctype html>
<html>
<head>
<meta charset ="utf-8">
<title>Robot Delivery System</title></head>
<body>
	<form action="deliveryTable.cgi" method="post">
		<h1>What would you like to have delivered?</h1>
		<table>
        {content}
		</table>
		<br />
		<h2>Cost: $</h2>
		<input type="text" name="cost" /><br />
		<h2>Delivery Method:</h2>
		<br><input type="radio" name="delivery_method" value="drone">Flying Drone ($10)
		<br><input type="radio" name="delivery_method" value="self driving car">Self Driving Car ($20)
		<br><input type="radio" name="delivery_method" value="giant robot">Giant Robot ($1000)
		<p><button type="submit">Submit</button></p>

	</form>
</body>
</html>"""

table = ""
table += "<tr><td> <input type = 'radio' name = 'item' value = Borscht>Borscht</td></tr>"
table += "<tr><td> <input type = 'radio' name = 'item' value = Coddle>Coddle</td></tr>"
table += "<tr><td> <input type = 'radio' name = 'item' value = Sweetbread>Sweetbread</td></tr>"
table += "<tr><td> <input type = 'radio' name = 'item' value = Blood Pudding>Blood Pudding</td></tr>"
table += "<tr><td> <input type = 'radio' name = 'item' value = Surströmming>Surströmming</td></tr>"

print(html.format(content = table))
