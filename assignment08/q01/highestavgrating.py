# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #8 Question #1
# What 5 movies have the highest average ratings? Show the movies and their ratings sorted by their average ratings.

import datetime
import numpy
import codecs

g = open('highestaveragerating.txt', 'w')

movieratings={}
averageratings={}
movieinfo={}
topmovies={}

with open('/Users/vneblitt/Documents/cs595-f13/assignment08/dataset/u.data', 'r') as f:
	movieratinginfo = f.readlines()
	for line in movieratinginfo:
		(userid, itemid, rating, timestamp) = line.split('\t')
		if itemid in movieratings:
			movieratings[itemid].append(int(rating))
		else:
			movieratings[itemid] = [int(rating)]
f.close()

for movie in movieratings:
	ratings = movieratings[movie]
	average = numpy.mean(ratings)
	averageratings[movie] = average

#stack overflow http://stackoverflow.com/questions/613183/python-sort-a-dictionary-by-value (11/10/2013)
for movieid in sorted(averageratings, key=averageratings.get, reverse=True)[0:10]:
	topmovies[movieid] = averageratings[movieid]

with (codecs.open('/Users/vneblitt/Documents/cs595-f13/assignment08/dataset/u.item','r', 'iso-8859-1')) as h:
	moviedata = h.readlines()
	for line in moviedata:
		(movieid, movietitle) = line.split('|')[0:2]
		movieinfo[movieid] = movietitle
h.close()

for movie in topmovies:
	g.write(movieinfo[movie] + ' ' + str(topmovies[movie]) + '\n')

g.close()