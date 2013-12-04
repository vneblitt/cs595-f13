# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #10 Question #1

import sys

sys.path.insert(0, '/Users/vneblitt/Documents/cs595-f13/assignment09/library')

import clusters

blognames,words,data=clusters.readfile('blogdata1.txt')

# row
print blognames[0]

# column
print words[3]

# junction
print data[0][3]


