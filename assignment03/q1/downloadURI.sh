#!/bin/bash

#curl http://www.usa.gov/Contact-Us.shtml

#pets="Phoebe Neo"

#for i in $pets; do
#echo $i
#done

mylinks=`cat testURIs.txt`
for link in $mylinks
do
	filename=`echo -n $link | md5`
	echo "Working on $link"
	curl $link > $filename
done