# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #8 Question #6
# Which 5 raters rated the most films? Show the raters' IDs and the number of films each rated.

g = open('prolificraters.txt', 'w')

movieraters={}
countingratings={}
topraters={}

with open('/Users/vneblitt/Documents/cs595-f13/assignment08/dataset/u.data', 'r') as f:
	movieratinginfo = f.readlines()
	for line in movieratinginfo:
		(userid, itemid, rating, timestamp) = line.split('\t')
		if userid in movieraters:
			movieraters[userid].append(int(rating))
		else:
			movieraters[userid] = [int(rating)]
f.close()
#print(movieraters)

for rater in movieraters:
	ratings = movieraters[rater]
	ratingscount = len(ratings)
	countingratings[rater] = ratingscount
#print(countingratings)

g.write('rater id, ' + 'number of ratings' + '\n')

#stack overflow http://stackoverflow.com/questions/613183/python-sort-a-dictionary-by-value (11/10/2013)
for rater in sorted(countingratings, key=countingratings.get, reverse=True)[0:5]:
	topraters[rater] = countingratings[rater]
	g.write(rater + ', ' + str(countingratings[rater]) + '\n')

g.close()