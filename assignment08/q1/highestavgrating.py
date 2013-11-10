# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #8 Question #1
# What 5 movies have the highest average ratings? Show the movies and their ratings sorted by their average ratings.

import datetime
import numpy
#g = open('highestaveragerating.txt', 'w')

movieratings={}
averageratings={}

with open('/Users/vneblitt/Documents/cs595-f13/assignment08/dataset/u.data', 'r') as f:
	movieratinginfo = f.readlines()
	for line in movieratinginfo:
		(userid, itemid, rating, timestamp) = line.split('\t')
		if itemid in movieratings:
			movieratings[itemid].append(int(rating))
		else:
			movieratings[itemid] = [int(rating)]
		#print('user id ' + userid)
		#g.write('item id: ' + itemid + ' rating: ' + rating + '\n')
		#print('date ' + datetime.datetime.fromtimestamp(int(timestamp)).strftime('%m-%d-%Y') + '\n')
		#print(datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S'))
		#print('timestamp ' + timestamp)
f.close()
print(movieratings)

for movie in movieratings:
	ratings = movieratings[movie]
	average = numpy.mean(ratings)
	averageratings[movie] = average
	
print(averageratings)

#g.close()