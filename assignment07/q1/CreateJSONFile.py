# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #7 Question #1

import json

#f = open('zachary.dat','r')
#g = open('zachary1.json', 'w')

adict = {}
adict["nodes"] = []
adict["edges"] = []

count = 0

with open('zachary.dat', 'r') as f:
   good = f.readlines()[41:]
for line in good:
	person = line.split()
	count = count + 1
	adict["nodes"].append({'name':str(count)})
    
print(adict)
#f.close()
#g.close()
    
