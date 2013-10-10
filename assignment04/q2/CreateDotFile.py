# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #4 Question #2

from os import listdir

# Access input file directory
mypath = '/Users/vneblitt/Documents/cs595-f13/assignment04/q1/linkingfiles/'
files = listdir(mypath)
files.remove('.DS_Store')

# Open the output file
s = open('/Users/vneblitt/Documents/cs595-f13/assignment04/q2/mydotfile.dot', 'w')
s.write('digraph spaghetti {\n')

# Iterate through input file directory
for file in files:
    f = open(mypath + file)
    mylines = f.readlines()

    site = mylines[1].strip('\n')
    links = mylines[3:]

    for link in links:
        link = link.strip()
        s.write('"' + site + '"' + ' -> ' + '"' + link + '"' + ' [ label = "' + site + ' to ' + link + '" ]; \n')

    f.close()

s.write('}')

s.close()

    
