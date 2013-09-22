import time

start = time.localtime()
print('Start time is: ' + time.asctime(start))


f = open('unpackedURLs.txt', 'r')
s = open('uniqueURIs.txt', 'w')

#read file in as a list
#Python documentation http://docs.python.org/3.3/tutorial/inputoutput.html

urilist = f.readlines()
print(len(urilist)) #test of number of URIs before

#convert list to a set
#from Stack Overflow http://stackoverflow.com/questions/6593979/how-to-convert-a-set-to-a-list-in-python

uriset = set(urilist)

print(len(uriset)) #test of number of URIs after

#write set contents to a file

for uri in uriset:
    s.write(uri)

f.close()
s.close()

finish = time.localtime()
print('Done. Finish time is: ' + time.asctime(finish))
