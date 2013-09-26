# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment #2 Question #3

# Converts the date returned by CarbonDate to a datetime object
# Compares it to local time

import datetime

f = open('testDateResults.txt', 'r')
s = open('URIAgeResults.txt', 'w')

for line in f:
    line = line.strip()
    try:
        (url, count, cd) = line.split('\t')
        currenttime = datetime.datetime.now()
        if cd:
            carbontime = datetime.datetime.strptime(cd, '%Y-%m-%dT%H:%M:%S')
            difference = currenttime - carbontime
            age = difference.days
            s.write(url + '\t' + count + '\t' + str(age) + '\n')
    except ValueError:
        pass

f.close()
s.close()


