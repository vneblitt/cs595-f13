# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #5 Question #1

import xml.etree.ElementTree as ET

s = open('friendcountreport.csv', 'w')

tree = ET.parse('/Users/vneblitt/Documents/FacebookGraphs/ValentinaNeblitt-Jones_1381612295-ego.graphml')
root = tree.getroot()

namespace = '{http://graphml.graphdrawing.org/xmlns}'

# structure: graph -> node -> data

nodes = root.findall(namespace + 'graph/' + namespace + 'node')

myfriends = 0

for node in nodes:
    data = node.findall(namespace + 'data')
    friends = 0
    myfriends = myfriends + 1

    for datum in data:
        if datum.attrib.get('key') == 'uid':
            uid = datum.text
        if datum.attrib.get('key') == 'friend_count':
            friends = datum.text

    if friends != 0:
        print(str(uid) + ',' + str(friends))
        s.write(str(uid) + ',' + str(friends) + '\n')

print('Valentina,' + str(myfriends))
s.write('Valentina,' + str(myfriends) + '\n')
