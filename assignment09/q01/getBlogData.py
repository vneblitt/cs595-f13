# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #10 Question #1

from bs4 import BeautifulSoup
import urllib2
import feedparser

d = feedparser.parse('http://f-measure.blogspot.com/feeds/posts/default')

# This is the blog title
print d.feed.title

# This is the blog link
# print d.feed.link

# This is the blog subtitle
# print d.feed.subtitle

# This is the title of entry 1
# print d.entries[0].title

# These are all the entry titles
for item in d.entries:
    print item.title
    
