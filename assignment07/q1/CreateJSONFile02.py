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

while networkx.number_connected_components(G) < 2:
	edgy = networkx.edge_betweenness_centrality(G)
	maxb = 0
	for edge in edgy:
		#print('key ' + str(edge) + ' value ' + str(edgy[edge]))
		if edgy[edge] > maxb:
			maxb = edgy[edge]
			maxedge = edge

	G.remove_edge(maxedge[0],maxedge[1])

result = json_graph.node_link_data(G)

g.write(json.dumps(result, indent=4))
g.close()

    
