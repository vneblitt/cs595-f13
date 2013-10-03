#!/bin/bash

#curl http://www.usa.gov/Contact-Us.shtml

#pets="Phoebe Neo"

#for i in $pets; do
#echo $i
#done

directory="/Users/vneblitt/Documents/cs595-f13/assignment03/raw"
mypages=`ls $directory`
for page in $mypages
do
	#filename=`echo -n $link | md5`
	echo "Working on $page"
	#echo $filename $link >> findingaid
	newfilename="/Users/vneblitt/Documents/cs595-f13/assignment03/processed/${page}.processed"
	lynx -dump -force_html $directory/$page > $newfilename
done