# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment 6 Question 1

data(karate)
# e <- edge.betweenness.community(karate)
plot.igraph(karate)
e1 <- edge.betweenness(karate)
e1ordered <- order(e1, decreasing=TRUE)
f <- e1ordered[-1]