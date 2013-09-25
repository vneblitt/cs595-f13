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
import math

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
                        category = 'IA'
                    elif (uri.find(yahoo1)!=-1 or uri.find(yahoo2)!=-1 or uri.find(yahoo3)!=-1):
                        type = 'Yahoo'
                        category = 'SE'
                    elif (uri.find(diigo)!=-1):
                        type = 'diigo'
                        category = 'Others'
                    elif (uri.find(bing)!=-1):
                        type = 'Bing'
                        category = 'SE'
                    elif (uri.find(wayback)!=-1):
                        type = 'Archive-It'
                        category = 'Others'
                    elif (uri.find(webArchiveNationalUK)!=-1):
                        type = 'UK National Archive'
                        category = 'Others'
                    elif (uri.find(webHarvest)!=-1):
                        type = 'Web Harvest'
                        category = 'Others'
                    elif (uri.find(webArchiveOrgUK)!=-1):
                        type = 'UK Web Archive'
                        category = 'Others'
                    elif (uri.find(webCitation)!=-1):
                        type = 'Web Citation'
                        category = 'Others'
                    elif (uri.find(cdlib)!=-1):
                        type = 'CD Lib'
                        category = 'Others'
                    elif (uri.find(archiefweb)!=-1):
                        type = 'ArchiefWeb'
                        category = 'Others'
                    elif (uri.find(mementoWayBack)!=-1):
                        type = 'Wayback Machine'
                        category = 'Others'
                    else:
                        type = 'Not Known'
                        category = 'Others'
                
                    memento = {}
                    memento["type"] = type
                    memento["category"] = category
                    memento["time"] = day_string
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
    
def isInPage(url,page):
	co = 'curl -i --silent -L -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30" "'+page+'"'
	page = commands.getoutput(co)
	loc = page.find(url)
	date = ""

	if(loc==-1):
		return False, date

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

	epoch = int(calendar.timegm(time.strptime(date, '%a, %d %b %Y %H:%M:%S %Z')))
	date = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(epoch))

	return True, date	

def getFirstAppearance(url, inurl):
	try:
		mementos = getMementos(inurl)
		if(len(mementos) == 0):
			return ""
		
		start = 0
		end = len(mementos)
		previous = -1
		i = 0
		foundbefore = False
		count = 0

		for mem in mementos:
			res, date = isInPage(url,mem["link"])

			if(res==True):
				break

		while(True):
			res, date = isInPage(url,mementos[i]["link"])

			if(res==True and i==0):
				return date
			if(int(math.fabs(previous-i))==0):
				return ""

			if( (res==True and int(math.fabs(previous-i))==1 and foundbefore == False) or (res==False and int(math.fabs(previous-i))==1 and foundbefore == True) ):
				return date

			previous = i
			if(res == False):
				start = i
				i = (end-start)/2 + start
				foundbefore = False

			else:
				end = i
				i = (end-start)/2 + start
				foundbefore = True
		
			count = count + 1

	except:
		print sys.exc_info() 

