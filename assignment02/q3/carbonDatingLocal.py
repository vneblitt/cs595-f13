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

	result = []
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
	print r
	return r
   

if(len(sys.argv)!=2):
	print "wrong format"
else:
	url = sys.argv[1]
	carbonDate(url)
