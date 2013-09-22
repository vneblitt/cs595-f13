# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #2 Question #2

import re
import time
import urllib.request

start = time.localtime()
print('Start time is: ' + time.asctime(start))


f = open('testTimeMapURIs.txt', 'r')
#s = open('uniqueURIs.txt', 'w')

uriprepend = 'http://mementoproxy.cs.odu.edu/aggr/timemap/link/'

for line in f:
    #print(uriprepend + line)
    try:
        a = uriprepend + line
        urllib.request.urlopen(a)
        print('TimeMaps found for ' + line)
    except urllib.error.HTTPError:
        print('No TimeMaps found for ' + line)
        pass


f.close()
#s.close()

finish = time.localtime()
print('Done. Finish time is: ' + time.asctime(finish))

