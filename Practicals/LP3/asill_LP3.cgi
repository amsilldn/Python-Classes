#! /usr/bin/env python
#Amanda Sill
#LP3
#Group 6

import cgitb
cgitb.enable()

import cgi

print('Content-type: text/html\n')

form = cgi.FieldStorage()

html = """<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Elvish Language Practice</title></head>
    <body>
    <img src={pic}>
	<h2>{out}</h2>
	<form method="post" action="asill_LP3.cgi">
            <p>Select a word to translate:
            <select name="word">
                <option>alda</option>
                <option>amon</option>
                <option>fenume</option>
                <option>hen</option>
                <option>huo</option>
                <option>lanne</option>
                <option>lapse</option>
                <option>liikuma</option>
                <option>lunte</option>
                <option>malle</option>
                <option>meoi</option>
                <option>olva</option>
                <option>parma</option>
                <option>quaare</option>
                <option>ramba</option>
                <option>silmo</option>
                <option>taal</option>
                <option>wilin</option>
                <option>yanta</option>
                <option>yulma</option>
            </select>
            </p>
            <p>Enter your translation: <input type="text" name="guess"></p>
        <button type="submit">Submit</button>
    </form>
    </body>
</html>"""

elvish = {"alda":"tree", "amon":"mountain", "fenume": "dragon", "hen":"eye", "huo":"dog", "lanne":"cloth", "lapse":"baby", "liikuma":"candle", "lunte":"ship", "malle":"road", "meoi":"cat", "olva":"plant", "parma":"book", "quaare":"hand", "ramba":"wall", "silmo":"moon", "taal":"foot", "wilin":"bird", "yanta":"bridge", "yulma":"cup"}

user = str(form.getfirst("word"))
guess = str(form.getfirst("guess"))

out = ""

image = "lp3img/" + str(form.getfirst("guess")) + ".jpg"

if (user, guess) in elvish.items():
    out = "That's correct!"
else:
    out = "Sorry, the correct word was " + elvish.get(user) + "."

print(html.format(pic = image, out = out))
