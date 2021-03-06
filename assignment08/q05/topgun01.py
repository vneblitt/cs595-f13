# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #8 Question #5
# What movie received ratings most like Top Gun? Which movie received ratings that were least like Top Gun (negative correlation)?

import sys
import pprint

sys.path.insert(0, '/Users/vneblitt/Documents/cs595-f13/assignment08/library')

import recommendations

g = open('topgun.txt', 'w')

prefs = recommendations.loadMovieLens(path='/Users/vneblitt/Documents/cs595-f13/assignment08/dataset')

answer = recommendations.calculateSimilarItems(prefs,n=1664)

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(answer['Top Gun (1986)'])

g.write(str(answer))
g.close()
