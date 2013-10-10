# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #4 Question #2

f = open('0bb6e775e10d833313f9bce6ef8711b0', 'r')
s = open('/Users/vneblitt/Documents/cs595-f13/assignment04/q2/mydotfile.dot', 'w')

mylines = f.readlines()

site = mylines[1].strip('\n')
links = mylines[3:]

s.write('digraph spaghetti {\n')

for link in mylines:
    link = link.strip()
    s.write('"' + site + '"' + ' -> ' + '"' + link + '"' + ' [ label = "' + site + ' to ' + link + '" ]; \n')

s.write('}')

f.close()
s.close()

    
