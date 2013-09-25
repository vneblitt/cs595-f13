import re
import time
import urllib2
import os
import sys
import datetime
import urllib
import simplejson
import calendar
import commands

from datetime import datetime

def getMementos(uri):
    uri = uri.replace(' ', '')
    orginalExpression = re.compile( r"<http://[A-Za-z0-9.:=/%-_ ]*>; rel=\"original\"," )
    mementoExpression = re.compile( r"<http://[A-Za-z0-9.:=/&,%-_ \?]*>;rel=\"(memento|first memento|last memento|first memento last memento|first last memento)\";datetime=\"(Sat|Sun|Mon|Tue|Wed|Thu|Fri), \d{2} (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (19|20)\d\d \d\d:\d\d:\d\d GMT\"" )
    zeroMementoExpression = re.compile(r"Resource: http://[A-Za-z0-9.:=/&,%-_ ]*")
    baseURI = 'http://mementoproxy.cs.odu.edu/aggr/timemap/link/'

    memento_list = []

    try:
	search_results = urllib.urlopen(baseURI+uri)
	the_page = search_results.read()

        timemapList = the_page.split('\n')

        count = 0
        for line in timemapList:
            if count <= 1:
                if line.find('Resource not in archive') > -1:
                    result = zeroMementoExpression.search( line )
                count = count + 1
                continue
            elif count == 2:
                result = orginalExpression.search( line )
                if result:
                     originalResult = result.group(0)
                     originalUri = originalResult[1:len(originalResult)-17]

            else:
		if(line.find("</memento")>0):
			line = line.replace("</memento", "<http://api.wayback.archive.org/memento")

		loc = line.find('>;rel="')
	        tofind = ';datetime="'
	        loc2 = line.find(tofind)
		if(loc!=-1 and loc2!=-1):
                    mementoURL = line[2:loc]
		    timestamp = line[loc2+len(tofind):line.find('"',loc2+len(tofind)+3)]

		    epoch = int(calendar.timegm(time.strptime(timestamp, '%a, %d %b %Y %H:%M:%S %Z')))
		    day_string = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(epoch))

                    uri = mementoURL
         
                    cdlib = 'webarchives.cdlib.org'
                    archiefweb = 'enterprise.archiefweb.eu'
                    webARchive= 'api.wayback.archive.org'
                    yahoo1 = 'uk.wrs.yahoo.com'
                    yahoo2 = 'rds.yahoo.com'
                    yahoo3 = 'wrs.yahoo.com'
                    diigo = 'www.diigo.com'
                    bing = 'cc.bingj.com'
                    wayback = 'wayback.archive-it.org'
                    webArchiveNationalUK = 'webarchive.nationalarchives.gov.uk'
                    webHarvest = 'webharvest.gov'
                    webArchiveOrgUK = 'www.webarchive.org.uk'
                    webCitation = 'webcitation.org'
                    mementoWayBack='memento.waybackmachine.org'
                    type = ''
                    category = ''
                    # @type uri str
                    if (uri.find(webARchive)!=-1):
                        type = 'Internet Archive'
			name = webARchive
                        category = 'IA'
                    elif (uri.find(yahoo1)!=-1 or uri.find(yahoo2)!=-1 or uri.find(yahoo3)!=-1):
                        type = 'Yahoo'
			name = 'yahoo.com'
                        category = 'SE'
                    elif (uri.find(diigo)!=-1):
                        type = 'diigo'
			name = diigo
                        category = 'Others'
                    elif (uri.find(bing)!=-1):
                        type = 'Bing'
			name = bing
                        category = 'SE'
                    elif (uri.find(wayback)!=-1):
                        type = 'Archive-It'
			name = wayback
                        category = 'Others'
                    elif (uri.find(webArchiveNationalUK)!=-1):
                        type = 'UK National Archive'
			name = webArchiveNationalUK
                        category = 'Others'
                    elif (uri.find(webHarvest)!=-1):
                        type = 'Web Harvest'
			name = webHarvest
                        category = 'Others'
                    elif (uri.find(webArchiveOrgUK)!=-1):
                        type = 'UK Web Archive'
			name = webArchiveOrgUK
                        category = 'Others'
                    elif (uri.find(webCitation)!=-1):
                        type = 'Web Citation'
			name = webCitation
                        category = 'Others'
                    elif (uri.find(cdlib)!=-1):
                        type = 'CD Lib'
			name = cdlib
                        category = 'Others'
                    elif (uri.find(archiefweb)!=-1):
                        type = 'ArchiefWeb'
			name = archiefweb
                        category = 'Others'
                    elif (uri.find(mementoWayBack)!=-1):
                        type = 'Wayback Machine'
			name = mementoWayBack
                        category = 'Others'
                    else:
			name = "other"
                        type = 'Not Known'
                        category = 'Others'
                
                    memento = {}
                    memento["type"] = type
                    memento["category"] = category
                    memento["time"] = day_string
                    memento["name"] = name
                    memento["link"] = mementoURL
		    memento["link"] = urllib.quote(memento["link"])
		    memento["link"] = memento["link"].replace("http%3A//", "http://")
		    memento["link"] = memento["link"][memento["link"].find("http://"):]
            
                    memento_list.append(memento)

		else:
			pass

            count = count + 1
        
    
    except urllib2.URLError:
        pass

    return memento_list
  

def getRealDate(url, memDate):   
	co = 'curl -i --silent -L -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30" "'+url+'"'
	page = commands.getoutput(co)
	date = ""

	to_find = "X-Archive-Orig-Last-modified: "
	loc = page.find(to_find)
	if(loc !=-1):
		end = page.find("\r", loc)
		date = page[loc+len(to_find):end]
		date = date.strip()

	if(date ==""):		
		to_find = "X-Archive-Orig-Date: "
		loc = page.find(to_find)
		if(loc !=-1):
			end = page.find("\r", loc)
			date = page[loc+len(to_find):end]
			date = date.strip()

	if(date ==""):
		date = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(memDate))	
	else:
		epoch = int(calendar.timegm(time.strptime(date, '%a, %d %b %Y %H:%M:%S %Z')))
		date = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(epoch))
	
	return date  

def getArchivesCreationDate(url):
	try:
		mementos = getMementos(url)
		if(len(mementos) == 0):
			result = []
			result.append(("Earliest", ""))
			result.append(("By_Archive", dict([])))
			return dict(result)
		archives = {}
		for memento in mementos:
			epoch = int(calendar.timegm(time.strptime(memento["time"], '%Y-%m-%dT%H:%M:%S')))
			if(memento["name"] not in archives):
				archives[memento["name"]] = {"link":memento["link"], "time": epoch}
			else:
				if(epoch<archives[memento["name"]]["time"]):
					archives[memento["name"]]["time"] = epoch
					archives[memento["name"]]["link"] = memento["link"]

		lowest = 99999999999
		link = ""

		limitEpoch = int(calendar.timegm(time.strptime("1995-01-01T12:00:00", '%Y-%m-%dT%H:%M:%S')))

		for archive in archives:
			date = getRealDate(archives[archive]["link"],archives[archive]["time"])
			epoch = int(calendar.timegm(time.strptime(date, '%Y-%m-%dT%H:%M:%S')))
			
			if(epoch<limitEpoch):
				archives[archive]["time"] = ""
				continue

			archives[archive]["time"] = date
			if(epoch<lowest):
				lowest = epoch

		lowest = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(lowest))

		result = []
		result.append(("Earliest", lowest))

		result2 = []
		for archive in archives:
			if(archives[archive]["time"]==""):
				continue
			result2.append((archive, str(archives[archive]["time"])))
		result.append(("By_Archive", dict(result2)))
		return dict(result)

	except:
		print sys.exc_info() 
		result = []
		result.append(("Earliest", ""))
		result.append(("By_Archive", dict([])))
		return dict(result)
