# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #10 Question #1

from bs4 import BeautifulSoup
from urllib2 import HTTPError
import urllib2
import time

f = open('feedlist.txt', 'w')

# These two are automatically in the list
firstfeed = 'http://f-measure.blogspot.com/feeds/posts/default'
secondfeed = 'http://ws-dl.blogspot.com/feeds/posts/default'

feedlist = []
feedlist.append(firstfeed)
feedlist.append(secondfeed)

while len(feedlist) <= 100:
    try:

        nextblog = 'http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117'

        html = urllib2.urlopen(nextblog).read()

        soup = BeautifulSoup(html)

        atomfeedurl = soup.find_all('link', attrs = {'type' : 'application/atom+xml'})[0].attrs['href']

    except HTTPError as h:
        pass

    except IndexError as i:
        pass

    if atomfeedurl:

        if atomfeedurl not in feedlist:

            print atomfeedurl
            feedlist.append(atomfeedurl)

    time.sleep(1)

for item in feedlist:
    f.write(item + '\n')

f.close()
