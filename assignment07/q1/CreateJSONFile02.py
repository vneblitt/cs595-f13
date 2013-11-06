# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #7 Question #1
# Create JSON file for graph after split

import json
import pprint
from networkx.readwrite import json_graph

pp = pprint.PrettyPrinter()

f = open('zachary1.json')

data = json.load(f)
# pp.pprint(data)
f.close()

G = json_graph.node_link_graph(data)

# Steps in R that I need to emulate
# data(karate)
# k <- karate

# repeat{
# kedge <- edge.betweenness(k)
# korder <- order(kedge, decreasing=TRUE)
# a <- korder[-1]
# b <- get.edge(k,a)
# k <- delete.edges(k, E(k,P=b))

# if (clusters(k)$no == 2) break()
# }


    
