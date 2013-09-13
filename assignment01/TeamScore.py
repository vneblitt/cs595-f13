# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #1 Question #2

from bs4 import BeautifulSoup
import urllib.request
import sys
import time

print("This is my answer for Assignment#1 Question#2")

school = sys.argv[1]
timeout = sys.argv[2]
uri = sys.argv[3]

while True:
    
    webscores = urllib.request.urlopen(uri).read()

    soup = BeautifulSoup(webscores)

#start parsing

    for div in soup.find_all('div', attrs = {'class' : 'mod-content'}):
        if school in div.get_text():
            break

#find visitor team information
    
    visitor = div.find_all('div', attrs = {'class' : 'team visitor'})[0]

    visitorname = visitor.find_all('a')[0]
    
    visitornamedisplay = visitorname.get_text()

    visitorscorebox = visitor.find_all('ul', attrs = {'class' : 'score'})[0]

    visitorscore = visitorscorebox.find_all('li')[-1]

    visitorscoredisplay = visitorscore.get_text()

#find home team information

    home = div.find_all('div', attrs = {'class' : 'team home'})[0]

    homename = home.find_all('a')[0]

    homenamedisplay = homename.get_text()

    homescorebox = home.find_all('ul', attrs = {'class' : 'score'})[0]

    homescore = homescorebox.find_all('li')[-1]

    homescoredisplay = homescore.get_text()

#print team names and corresponding scores

    print(visitornamedisplay +': '+ visitorscoredisplay + ', ' + homenamedisplay +': '+ homescoredisplay)

    time.sleep(int(timeout))
