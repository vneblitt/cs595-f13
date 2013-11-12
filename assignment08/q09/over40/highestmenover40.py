# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #8 Question #9 - Over 40
# What movie was rated highest on average by men over 40?

import codecs
import numpy

g = open('highestmenover40.txt', 'w')

theguys=[]
movieratings={}
averageratings={}
movieinfo={}


# Parse u.user to get the userid, age, and gender and create a list of userids that only contain men over 40
with open('/Users/vneblitt/Documents/cs595-f13/assignment08/dataset/u.user', 'r') as j:
	userdata = j.readlines()
	for line in userdata:
		(userid, age, gender) = line.split('|')[0:3]
		if gender == 'M':
			if int(age) > 40:
				theguys.append(userid)

# Create a dictionary of movies and ratings only if the user is a men over 40
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
for movieid in sorted(averageratings, key=averageratings.get, reverse=True)[0:25]:
	g.write(movieinfo[movieid] + ' ' + str(averageratings[movieid]) + '\n')

g.close()