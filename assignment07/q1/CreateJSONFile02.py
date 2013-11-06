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


    
