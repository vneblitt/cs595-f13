# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #8 Question #4
# What 5 movies were rated the highest on average by men? Show the movies and their ratings sorted by ratings.

import codecs
import numpy

g = open('highestmen.txt', 'w')

userinfo={}
theguys=[]
movieratings={}
averageratings={}
movieinfo={}


# Parse u.user to get the userid, age, and gender (only need userid and gender)
with open('/Users/vneblitt/Documents/cs595-f13/assignment08/dataset/u.user', 'r') as j:
	userdata = j.readlines()
	for line in userdata:
		(userid, age, gender) = line.split('|')[0:3]
		userinfo[userid] = gender

# Create a list of userids that only belong to women
for user in userinfo:
	if userinfo[user] == 'M':
		theguys.append(user)

# Create a dictionary of movies and ratings only if the user is a man
with open('/Users/vneblitt/Documents/cs595-f13/assignment08/dataset/u.data', 'r') as f:
	movieratinginfo = f.readlines()
	for line in movieratinginfo:
		(userid, itemid, rating, timestamp) = line.split('\t')
		if userid in theguys:
			if itemid in movieratings:
				movieratings[itemid].append(int(rating))
			else:
				movieratings[itemid] = [int(rating)]
f.close()

# Calculate the average rating for each movie
for movie in movieratings:
	ratings = movieratings[movie]
	average = numpy.mean(ratings)
	averageratings[movie] = average

with (codecs.open('/Users/vneblitt/Documents/cs595-f13/assignment08/dataset/u.item','r', 'iso-8859-1')) as h:
	moviedata = h.readlines()
	for line in moviedata:
		(movieid, movietitle) = line.split('|')[0:2]
		movieinfo[movieid] = movietitle
h.close()

#stack overflow http://stackoverflow.com/questions/613183/python-sort-a-dictionary-by-value (11/10/2013)
for movieid in sorted(averageratings, key=averageratings.get, reverse=True)[0:16]:
	g.write(movieinfo[movieid] + ' ' + str(averageratings[movieid]) + '\n')

g.close()