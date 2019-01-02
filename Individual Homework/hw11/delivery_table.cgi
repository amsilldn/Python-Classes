#! /usr/bin/env python3

print('Content-type: text/html\n')

import MySQLdb

string = "i211s18_asill"
password = "my+sql=i211s18_asill"

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

htlm = """
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Robot Delivery System Confirmation</title></head>
<body>
    <h1>Robot Delivery System Confirmation</h1>
    <p>You have selected to have a Book delivered by drone.</p>
    <p>Your total comes to $20</p>
    <h2>Delivery Records</h2>
    <table border="1">
        <tr><th>Item</th><th>Cost</th><th>Method</th><th>Shipping</th></tr>
        {content}
    </table>
</body>
</html>"""

form = cgi.FieldStorage()
item = form.getfirst('item')
cost = form.getfirst('cost')
price = int(cost)
price = int(price)
dm = form.getfirst('delivery_method')

table = ""

if dm == "drone":
  method = "drone"
  total += 10
elif dm == "self driving car":
  method = "self driving car"
  total += 20
else:
  method = "giant robot"
  total += 1000

 try:
    SQL = "INSERT INTO Deliveries (Item, Cost, Method, Shipping)"
    SQL += "VALUES('" + str(item) "','" + str(cost)  + "','" + str(dm) + "','" + str(price) + ");"
    cursor.execute(SQL)
    db_con.commit()

except Exception as e:
    print('<p>Somthing went wrong with the SQL!</p>')
    print(SQL, "\nError:", e)

else:
    try:
        SQL = "SELECT * FROM Deliveries;"
        cursor.execute(SQL)
        results = cursor.fetchall()

    except Exception as e:
        print('<p>Somthing went wrong with the SQL!</p>')
        print(SQL, "\nError:", e)

    else:
        for result in results:
    		table += "<tr>"
    		for entry in result:
    			table += "<td align='center'>" + str(entry) + "</td>"
            table += "</tr>"

print(html.format(item = item, method = dm, total = price, content = table))
