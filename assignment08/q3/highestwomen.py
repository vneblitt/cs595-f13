# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #8 Question #3
# What 5 movies were rated the highest on average by women? Show the movies and their ratings sorted by ratings.

import codecs

# g = open('mostratings.txt', 'w')

movieratings={}
userinfo={}
# countingratings={}
# movieinfo={}

with open('/Users/vneblitt/Documents/cs595-f13/assignment08/dataset/u.data', 'r') as f:
	movieratinginfo = f.readlines()
	for line in movieratinginfo:
		(userid, itemid, rating, timestamp) = line.split('\t')
		if itemid in movieratings:
			movieratings[itemid].append(int(rating))
		else:
			movieratings[itemid] = [int(rating)]
f.close()

with open('/Users/vneblitt/Documents/cs595-f13/assignment08/dataset/u.user', 'r') as j:
	userdata = j.readlines()
	for line in userdata:
		(userid, age, gender) = line.split('|')[0:3]
		userinfo[userid] = gender
print(userinfo)

# for movie in movieratings:
# 	ratings = movieratings[movie]
# 	ratingscount = len(ratings)
# 	countingratings[movie] = ratingscount
# #print(countingratings)
# 
# with (codecs.open('/Users/vneblitt/Documents/cs595-f13/assignment08/dataset/u.item','r', 'iso-8859-1')) as h:
# 	moviedata = h.readlines()
# 	for line in moviedata:
# 		(movieid, movietitle) = line.split('|')[0:2]
# 		movieinfo[movieid] = movietitle
# h.close()
# 
# #stack overflow http://stackoverflow.com/questions/613183/python-sort-a-dictionary-by-value (11/10/2013)
# for movieid in sorted(countingratings, key=countingratings.get, reverse=True)[0:5]:
# 	g.write(movieinfo[movieid] + ' ' + str(countingratings[movieid]) + '\n')
# 
# g.close()