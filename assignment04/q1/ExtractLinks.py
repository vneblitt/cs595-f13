# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #4 Question #1

from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse

f = open('inputfile.txt', 'r')

for line in f:

    (rawfile, uri) = line.split()
    print("Working on " + rawfile)
    g = open('/Users/vneblitt/Documents/cs595-f13/assignment03/raw/' + rawfile)
    piece = urlparse (uri)


    first = g.read()
    soup = BeautifulSoup(first)
    s = open('/Users/vneblitt/Documents/cs595-f13/assignment04/q1/' + rawfile, 'w')
    s.write('site:' + '\n')
    s.write(uri + '\n')
    s.write('links:' + '\n')

    for link in soup.find_all('a'):
        a = link.get('href') #full link or link fragment
        b = urlparse(a) #parsed link

        if not b.scheme: #is it relative?
            if not b.path:
                c = (str(piece.scheme) + '://' + str(piece.netloc) + '/' + '\n')
                s.write(c)
            else:
                c = (str(piece.scheme) + '://' + str(piece.netloc) + str(b.path) + '\n')
                s.write(c)
        elif b.scheme == 'javascript':
            pass
        else:
            s.write(a + '\n')

    s.close()

    g.close()

f.close()
    
