# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment 6 Question 1

data(karate)
k <- karate
plot.igraph(k)

repeat{
kedge <- edge.betweenness(k)
korder <- order(kedge, decreasing=TRUE)
a <- korder[-1]
b <- get.edge(k,a)
k <- delete.edges(k, E(k,P=b))
plot.igraph(k)

if (clusters(k)$no == 2) break()
}