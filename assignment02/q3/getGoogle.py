import sys
import os
import calendar
import time
import commands
from getLowest import getLowest

def getGoogleCreationDate(url):
	inurl_creation_date = ""
	try:
		query = 'https://www.google.com/search?hl=en&tbo=d&tbs=qdr:y15&q=inurl:'+url+'&oq=inurl:'+url
		page = commands.getoutput('curl --silent -L -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30" "'+query+'"')
		loc = 0	
		lowest_date = 99999999999
		while(True):
			start_str = 'class="f std" >'
			loc = page.find(start_str,loc)
			fin = page.find("</span>", loc)
			if(loc==-1):
				break
			timestamp = page[loc+len(start_str):fin]
			epoch = int(calendar.timegm(time.strptime(timestamp, '%b %d, %Y')))

			limitEpoch = int(calendar.timegm(time.strptime("1995-01-01T12:00:00", '%Y-%m-%dT%H:%M:%S')))
			if(epoch<limitEpoch):
				continue

			if(epoch<lowest_date):
				lowest_date = epoch
			inurl_creation_date = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(lowest_date))
			loc = fin
	except:
		pass

	search_creation_date = ""
	try:
		query = 'https://www.google.com/search?hl=en&tbo=d&tbs=qdr:y15&q='+url
		page = commands.getoutput('curl --silent -L -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30" "'+query+'"')
		loc = 0	
		lowest_date = 99999999999
		while(True):
			start_str = 'class="f std" >'
			loc = page.find(start_str,loc)
			fin = page.find("</span>", loc)
			if(loc==-1):
				break
			timestamp = page[loc+len(start_str):fin]
			epoch = int(calendar.timegm(time.strptime(timestamp, '%b %d, %Y')))

			limitEpoch = int(calendar.timegm(time.strptime("1995-01-01T12:00:00", '%Y-%m-%dT%H:%M:%S')))
			if(epoch<limitEpoch):
				continue

			if(epoch<lowest_date):
				lowest_date = epoch
			search_creation_date = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(lowest_date))
			loc = fin
	except:
		pass

	return getLowest([search_creation_date,inurl_creation_date])

