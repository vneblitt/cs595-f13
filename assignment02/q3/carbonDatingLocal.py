import json
from ordereddict import OrderedDict
import simplejson
from getTopsy import getTopsyCreationDate
from getBitly import getBitlyCreationDate
from getArchives import getArchivesCreationDate
from getGoogle import getGoogleCreationDate
from getBacklinks import *
from getLowest import getLowest
from getLastModified import getLastModifiedDate
import sys
import os
import time

#---------------------------------------------------------------------------------------#
#--------------------------Function call to aggregate results---------------------------#
#---------------------------------------------------------------------------------------#

def carbonDate(url):
	print"\n\n\n\n\n--------------------------------\n--- Getting Creation dates for:\n"+url+"\n\n"

	bitly = getBitlyCreationDate(url)
	print "Done Bitly"
	archives = getArchivesCreationDate(url)
	print "Done Archives"
	topsy = getTopsyCreationDate(url)
	print "Done Topsy"
	google = getGoogleCreationDate(url)
	print "Done Google"
	backlink = getBacklinksFirstAppearanceDates(url)
	print "Done Backlinks"
	lastmodified = getLastModifiedDate(url)
	print "Done Last Modified"
	lowest = getLowest([bitly,topsy,google,backlink,lastmodified,archives["Earliest"]])
	print "Got Lowest"

	'''result = []
	result.append(("URI", url))
	result.append(("Estimated Creation Date", lowest))
	result.append(("Last Modified", lastmodified))
	result.append(("Bitly.com", bitly))
	result.append(("Topsy.com", topsy))
	result.append(("Backlinks", backlink))
	result.append(("Google.com", google))
	result.append(("Archives", archives))
	values = OrderedDict(result)
	r = json.dumps(values, sort_keys=False, indent=2, separators=(',', ': '))
	print r'''
	return lowest
   

if(len(sys.argv)!=3):
	print "wrong format"
else:
        start = time.localtime()
        print 'Start time is: ' + time.asctime(start)
        
        inputfile = sys.argv[1]
        outputfile = sys.argv[2]
        f = open(inputfile)
        s = open(outputfile, 'w')
        for line in f:
                line = line.strip()
                (url, count) = line.split(', ')
                cd = carbonDate(url)
                s.write(url + '\t' + count + '\t' + cd + '\n')
                s.flush()
                os.fsync(s.fileno())
        f.close()
        s.close()

        finish = time.localtime()
        print 'Done. Finish time is: ' + time.asctime(finish)

#Flush output
#http://stackoverflow.com/questions/230751/how-to-flush-output-of-python-print
        



