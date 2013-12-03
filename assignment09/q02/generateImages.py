# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment 9 Question 2

import sys

sys.path.insert(0, '/Users/vneblitt/Documents/cs595-f13/assignment09/library')

import clusters

# Create clusters
blognames,words,data=clusters.readfile('blogdata1.txt')
clust=clusters.hcluster(data)

# Create ASCII dendrogram
clusters.printclust(clust,labels=blognames)

# Create Nicer dendrogram with PIL
clusters.drawdendrogram(clust,blognames,jpeg='blogclust.jpg')