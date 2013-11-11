# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #8 Question #2
# What 5 movies received the most ratings? Show the movies and the number of ratings sorted by number of ratings.

import codecs

g = open('mostratings.txt', 'w')

movieratings={}
countingratings={}
movieinfo={}

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
	ratingscount = len(ratings)
	countingratings[movie] = ratingscount
#print(countingratings)

with (codecs.open('/Users/vneblitt/Documents/cs595-f13/assignment08/dataset/u.item','r', 'iso-8859-1')) as h:
	moviedata = h.readlines()
	for line in moviedata:
		(movieid, movietitle) = line.split('|')[0:2]
		movieinfo[movieid] = movietitle
h.close()

#stack overflow http://stackoverflow.com/questions/613183/python-sort-a-dictionary-by-value (11/10/2013)
for movieid in sorted(countingratings, key=countingratings.get, reverse=True)[0:5]:
	g.write(movieinfo[movieid] + ' ' + str(countingratings[movieid]) + '\n')

g.close()