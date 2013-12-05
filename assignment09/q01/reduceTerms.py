# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #10 Question #1

import sys

sys.path.insert(0, '/Users/vneblitt/Documents/cs595-f13/assignment09/library')

import clusters

blognames,words,data=clusters.readfile('blogdata.txt')

# row
# print 'blog name: ' + blognames[0]

# column
# print 'term: ' + words[3]

# junction
# print 'value: ' + str(data[0][3])

# print 'number of blogs: ' + str(len(blognames))
# print 'number of words: ' + str(len(words))

wordsums={}

for j in range(len(words)):
	sum = 0
	for i in range (len(blognames)):
		sum = sum + data[i][j]
	# print words[j] + ' ' + str(sum)
	wordsums[j] = int(sum)
	
# print wordsums

a = sorted(wordsums, key=wordsums.get, reverse=True)[0:500]

# print (len(a))

# print a

print 'Blog',

for m in range(len(words)):
	if m in a:
		print '\t' + words[m],
print

for i in range(len(blognames)):
	print blognames[i],
		
	for j in range(len(words)):
		if j in a:
			print '\t' + str(int(data[i][j])),
			
	print