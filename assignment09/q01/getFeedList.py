# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #10 Question #1

from bs4 import BeautifulSoup
import urllib2
import feedparser
import re

# These two are automatically in the list
firstfeed = 'http://f-measure.blogspot.com/feeds/posts/default'
secondfeed = 'http://ws-dl.blogspot.com/feeds/posts/default'

print firstfeed
print secondfeed

nextblog = 'http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117'

html = urllib2.urlopen(nextblog).read()

soup = BeautifulSoup(html)

atomfeedurl = soup.find_all('link', attrs = {'type' : 'application/atom+xml'})[0].attrs['href']

print atomfeedurl


