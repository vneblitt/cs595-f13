# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment 10

import os
import feedparser
import docclass

os.unlink('gimmelego.db')

# The first 50 entries manually classified
cl=docclass.classifier(docclass.getwords)

cl.setdb('gimmelego.db')

d = feedparser.parse('http://gimmelego.blogspot.com/feeds/posts/default?max-results=100')

cl.train(d.entries[0].content[0].value, 'original')
cl.train(d.entries[1].content[0].value, 'original')
cl.train(d.entries[2].content[0].value, 'books')
cl.train(d.entries[3].content[0].value, 'sets')
cl.train(d.entries[4].content[0].value, 'events')
cl.train(d.entries[5].content[0].value, 'events')
cl.train(d.entries[6].content[0].value, 'original')
cl.train(d.entries[7].content[0].value, 'sets')
cl.train(d.entries[8].content[0].value, 'sets')
cl.train(d.entries[9].content[0].value, 'books')
cl.train(d.entries[10].content[0].value, 'events')
cl.train(d.entries[11].content[0].value, 'sets')
cl.train(d.entries[12].content[0].value, 'original')
cl.train(d.entries[13].content[0].value, 'original')
cl.train(d.entries[14].content[0].value, 'events')
cl.train(d.entries[15].content[0].value, 'events')
cl.train(d.entries[16].content[0].value, 'sets')
cl.train(d.entries[17].content[0].value, 'sets')
cl.train(d.entries[18].content[0].value, 'minifigures')
cl.train(d.entries[19].content[0].value, 'original')
cl.train(d.entries[20].content[0].value, 'sets')
cl.train(d.entries[21].content[0].value, 'sets')
cl.train(d.entries[22].content[0].value, 'sets')
cl.train(d.entries[23].content[0].value, 'sets')
cl.train(d.entries[24].content[0].value, 'sets')
cl.train(d.entries[25].content[0].value, 'original')
cl.train(d.entries[26].content[0].value, 'sets')
cl.train(d.entries[27].content[0].value, 'original')
cl.train(d.entries[28].content[0].value, 'sets')
cl.train(d.entries[29].content[0].value, 'awards')
cl.train(d.entries[30].content[0].value, 'sets')
cl.train(d.entries[31].content[0].value, 'awards')
cl.train(d.entries[32].content[0].value, 'awards')
cl.train(d.entries[33].content[0].value, 'sets')
cl.train(d.entries[34].content[0].value, 'sets')
cl.train(d.entries[35].content[0].value, 'original')
cl.train(d.entries[36].content[0].value, 'sets')
cl.train(d.entries[37].content[0].value, 'sets')
cl.train(d.entries[38].content[0].value, 'market')
cl.train(d.entries[39].content[0].value, 'original')
cl.train(d.entries[40].content[0].value, 'events')
cl.train(d.entries[41].content[0].value, 'sets')
cl.train(d.entries[42].content[0].value, 'original')
cl.train(d.entries[43].content[0].value, 'sets')
cl.train(d.entries[44].content[0].value, 'minifigures')
cl.train(d.entries[45].content[0].value, 'original')
cl.train(d.entries[46].content[0].value, 'summary')
cl.train(d.entries[47].content[0].value, 'original')
cl.train(d.entries[48].content[0].value, 'sets')
cl.train(d.entries[49].content[0].value, 'market')

# The second 50 entries classified using Fisher

cl = docclass.fisherclassifier(docclass.getwords)

for i in range(50, 100):
	category = cl.classify(d.entries[i].content[0].value)
	print d.entries[i].title + ' : ' + category
	
for i in range(50, 100):
	for cat in categories:
		print cl.cprob(d.entries[i].title, cat)















