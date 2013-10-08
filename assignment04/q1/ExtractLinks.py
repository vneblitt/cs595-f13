# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #4 Question #1

from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse

f = open('testinputfile.txt', 'r')
s = open('testoutputfile.txt', 'w')

for line in f:
    try:
        first = urllib.request.urlopen(line).read()
        piece = urlparse (line)
        soup = BeautifulSoup(first)
        #print('Working on ' + line)

        for link in soup.find_all('a'):
            a = link.get('href')
            b = urlparse(a)

            if not b.scheme:
                c = (str(piece.scheme) + '://' + str(piece.netloc) + '/' + str(b.path) + '\n')
                s.write(c)

            else:
                s.write(a + '\n')
    except urllib.error.HTTPError as e:
        print(line + ' ' + str(e))
    except UnicodeEncodeError as l:
        print(line + ' ' + str(l))

f.close()
s.close()
    
