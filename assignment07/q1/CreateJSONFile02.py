# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #7 Question #1
# Create JSON file for graph after split

import json
import pprint
import networkx
from networkx.readwrite import json_graph

pp = pprint.PrettyPrinter()

f = open('zachary1.json')
g = open('zachary2.json', 'w')

data = json.load(f)
# pp.pprint(data)
f.close()

G = json_graph.node_link_graph(data)

# Steps in R that I need to emulate
# data(karate)
# k <- karate

# repeat{
# kedge <- edge.betweenness(k)
while networkx.number_connected_components(G) < 2:
	edgy = networkx.edge_betweenness_centrality(G)
# pp.pprint(edgy)
	maxb = 0
	for edge in edgy:
		#print('key ' + str(edge) + ' value ' + str(edgy[edge]))
		if edgy[edge] > maxb:
			maxb = edgy[edge]
			maxedge = edge
# print(maxb)
# print(maxedge)
	G.remove_edge(maxedge[0],maxedge[1])

# pp.pprint(G.edges())

# korder <- order(kedge, decreasing=TRUE)
# a <- korder[-1]
# b <- get.edge(k,a)
# k <- delete.edges(k, E(k,P=b))

# if (clusters(k)$no == 2) break()
# }

result = json_graph.node_link_data(G)

# print(json.dumps(result, indent=4))

g.write(json.dumps(result, indent=4))
g.close()

    
