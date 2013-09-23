# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #2 Question #2

import re
import time
import urllib.request

start = time.localtime()
print('Start time is: ' + time.asctime(start))

#misses the first and last memento
#pattern = re.compile('rel="([a-z]*)memento"')

#returns zero even though not true
#pattern = re.compile('rel="memento" | rel="first memento" | rel="last memento"')

#invalid syntax
#pattern = re.compile(('rel="memento") | (rel="first memento") | (rel="last memento")')

pattern = re.compile('rel="[(first | last)]*memento"')

f = open('testTimeMapURIs.txt', 'r')
s = open('timeMapResults.txt', 'w')

uriprepend = 'http://mementoproxy.cs.odu.edu/aggr/timemap/link/'

for line in f:
    #print(uriprepend + line)
    try:
        a = uriprepend + line
        r = urllib.request.urlopen(a)
        #print('TimeMaps found for ' + line)
        timemap = r.read()
        c = pattern.findall(timemap.decode('utf-8'))
        #print(line.rstrip() + " produces " + str(len(c)) + " timemaps")
        s.write(line.rstrip() + " produces " + str(len(c)) + " timemaps\n")
    except urllib.error.HTTPError:
        #print('No TimeMaps found for ' + line)
        s.write(line.rstrip() + " produces zero timemaps\n")
        pass


f.close()
s.close()

finish = time.localtime()
print('Done. Finish time is: ' + time.asctime(finish))

#Pages Consulted
#HTTP Response Objects
#http://docs.python.org/3.3/library/http.client.html#httpresponse-objects
#Regular Expressions
#http://docs.python.org/3/howto/regex.html
#Byte Strings
#http://stackoverflow.com/questions/6224052/what-is-the-difference-between-a-string-and-a-byte-string

