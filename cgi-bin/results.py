#!/usr/bin/python

import cgi
import cgitb

cgitb.enable(display=0, logdir="index.html")
#imports cgi and directions to html code

import urllib

# print("Content-Type: text/html")    # HTML is following
# print(display=0, logdir="/index.html")                        # blank line, end of headers

form = cgi.FieldStorage()
#sets the output form the html file as a dictionary named "form"

if form.getvalue("color"):
	color = form.getvalue("color")
else:
	color = "Not set"
if form.getvalue("place"):
	place = form.getvalue("place")
else:
	place = "Not set"
if form.getvalue("activity"):
	activity = form.getvalue("activity")
else:
	activity = "Not set"
if form.getvalue("song"):
	song = form.getvalue("song")
else:
	song = "Not set"
if form.getvalue("food"):
	foood = form.getvalue("food")
else:
	food = "Not set"
#sets all the answers from the html file as their respective variable names
#e.g, color = red if the user chose red. 

dlist = [color, place, food, activity, song]
#makes a list out of all of the outputs

def addshittothedic(d):
#basically hard codes all the outputs and adds values to each emotion
	emo = {"joy":0, "sadness":0, "anger":0, "disgust":0,"fear":0};
	if d[0] == "red":
		emo["anger"] += 3
		emo["disgust"] += 1
	if d[0] == "orange":
		emo["joy"] += 3
		emo["anger"] += 1
	if d[0] == "yellow":
		emo["joy"] += 3
		emo["fear"] += 1
	if d[0] == "green":
		emo["disgust"] += 3
		emo["fear"] += 2
	if d[0] == "blue":
		emo["sadness"] += 3
		emo["fear"] += 1
	if d[0] == "purple":
		emo["joy"] += 1
		emo["fear"] += 3
	if d[0] == "pink":
		emo["joy"] += 2
		emo["disgust"] += 2
	if d[0] == "brown":
		emo["disgust"] += 1
		emo["fear"] += 1
		emo["sadness"] == 1
	if d[0] == "black":
		emo["anger"] += 2
		emo["sadness"] += 2
	if d[1] == "bedroom":
		emo["sadness"] += 2
		emo["disgust"] += 1
	if d[1] == "sunny_park":
		emo["joy"] += 3
	if d[1] == "gym":
		emo["anger"] += 2
		emo["disgust"] += 2
	if d[1] == "food_court":
		emo["sadness"] += 3
		emo["fear"] += 2
	if d[1] == "beach":
		emo["joy"] += 3
		emo["fear"] += 1
	if d[1] == "mountain":
		emo["fear"] += 2
		emo["anger"] += 2
	if d[1] == "city":
		emo["fear"] += 2
		emo["disgust"] += 2
	if d[1] == "forest":
		emo["fear"] += 2
		emo["anger"] += 2
	if d[1] == "suburban_house":
		emo["joy"] += 2
		emo["anger"] += 2
	if d[2] == "sweets":
		emo["sadness"] += 2
		emo["sadness"] += 2
	if d[2] == "spicy":
		emo["angry"] += 2
		emo["disgust"] += 2	
	if d[2] == "salty":
		emo["fear"] += 2
		emo["anger"] += 2
	if d[2] == "caffeine":
		emo["fear"] += 2
		emo["sadness"] += 2
	if d[2] == "crunchy":
		emo["anger"] += 2
	if d[2] == "chocolate":
		emo["joy"] += 2
	if d[2] == "starch":
		emo["joy"] += 2
		emo["anger"] += 2
	if d[2] == "ice_cream":
		emo["sadness"] += 3
	if d[2] == "cheese":
		emo["disgust"] += 2
		emo["joy"] += 2
	if d[3] == "sleeping_in":
		emo["sadness"] += 2
		emo["anger"] += 2
	if d[3] == "partying":
		emo["fear"] += 2
		emo["joy"] += 2
	if d[3] == "homework":
		emo["sadness"] += 2
		emo["fear"] += 2
	if d[3] == "watching_tv":
		emo["sadness"] += 2
		emo["anger"] += 2
	if d[3] == "hiking":
		emo["joy"] += 3
		emo["fear"] += 1
	if d[3] == "eating":
		emo["fear"] += 2
		emo["anger"] += 2
	if d[3] == "listen_to_music":
		emo["sadness"] += 3
	if d[3] == "road_trip":
		emo["fear"] += 2
		emo["joy"] += 2
	if d[4] == "how_far_ill_go":
		emo["anger"] += 1
		emo["joy"] += 3
	if d[4] == "fighter":
		emo["anger"] += 3
		emo["fear"] += 2
	if d[4] == "love_on_top":
		emo["anger"] += 1
		emo["joy"] += 3
	if d[4] == "i_love_it":
		emo["fear"] += 1
		emo["joy"] += 2
	if d[4] == "blank_space":
		emo["disgust"] += 3
		emo["anger"] += 2
		emo["sadness"] += 1
	if d[4] == "someone_like_you":
		emo["sadness"] += 3
		emo["fear"] += 2
	if d[4] == "love_the_way_you_lie":
		emo["anger"] += 3
		emo["sadness"] += 2
	if d[4] == "boulevard_of_broken_dreams":
		emo["sadness"] += 2
		emo["fear"] += 1
		emo["anger"] += 1
	if d[4] == "see_you_again":
		emo["sadness"] += 3
		emo["fear"] += 1
	return emo

def getavg(emo):
	#makes the values for each emotion into a percentage float. 
	total = 0
	total += emo["joy"]
	total += emo["sadness"]
	total += emo["fear"]
	total += emo["anger"]
	total += emo["disgust"]
	emo["joy"] = emo["joy"]/total
	emo["sadness"] = emo["joy"]/total
	emo["fear"] = emo["fear"]/total
	emo["anger"] = emo["anger"]/total
	emo["disgust"] = emo["disgust"]/total
	return emo


numlist = addshittothedic(dlist)
result = getavg(numlist)

movies= ["home alone", "inside out", "kungfu panda"]

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2> Recommended Movies:</h2>")
for movie in movies:
	print(movie + "</br>")
print ("</body>")
print ("</html>")

# import urllib.request
# page = urllib.request.urlopen("recommendations.html").read()
# page = page.read().decode("utf8")
# print(page)


