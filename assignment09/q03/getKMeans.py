# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment 9 Question 3


import sys

sys.path.insert(0, '/Users/vneblitt/Documents/cs595-f13/assignment09/library')

import clusters

blognames,words,data=clusters.readfile('/Users/vneblitt/Documents/cs595-f13/assignment09/q01/blogdata1.txt')

print 'k=5'
kclust=clusters.kcluster(data,k=5)

print 'k=10'
kclust=clusters.kcluster(data,k=10)

print 'k=20'
kclust=clusters.kcluster(data,k=20)