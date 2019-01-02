#! /usr/bin/env python3
#Amanda Sill
#Group 6
print('Content-type: text/html\n')

import cgitb
cgitb.enable()

import cgi

form = cgi.FieldStorage()

html="""
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Robot Delivery System Confirmation</title></head>
    <body>
    <h1>Robot Delivery System Confirmation</h1>
    <p>You have selected to have a {delivery} delivered by {method}.</p>
<p>Your total comes to ${total}</p>
    </body>
</html>"""

dm = form.getfirst("delivery_method")
delivery = form.getfirst("delivery")
cost = form.getfirst("cost", 0)
total = int(cost)

if dm == "drone":
  method = "drone"
  total += 10
elif dm == "self driving car":
  method = "self driving car"
  total += 20
else:
  method = "giant robot"
  total += 1000


print(html.format(delivery = delivery, method = method, total = total))
