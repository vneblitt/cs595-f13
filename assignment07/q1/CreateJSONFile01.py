# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #7 Question #1

import json
import pprint

g = open('zachary1.json', 'w')
pp = pprint.PrettyPrinter()

adict = {}
adict["nodes"] = []
adict["links"] = []

id = 0 # name

with open('zachary.dat', 'r') as f:
   good = f.readlines()[41:]
for line in good:
	person = line.split()
	id = id + 1 # generates name
	adict["nodes"].append({'id':str(id)})
	for i in range(0, len(person)):
		weight = int(person[i])
		source = id - 1
		target = i
		if weight != 0:
			adict["links"].append({'source': source, 'target': target, 'weight':weight})
			
pp.pprint(adict)
output = json.dumps(adict, indent=4)
g.write(output)

f.close()
g.close()
    
