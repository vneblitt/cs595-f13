import urllib.request
import urllib.parse
import urllib.error
import http.client
import time

start = time.localtime()
print('Start time is: ' + time.asctime(start))

#a = urllib.request.urlopen('http://goo.gl/LhYg3')

f = open('tweetlink.txt', 'r')
s = open('unpackedURLs.txt', 'w')

#try:
#    print(a.geturl())

#except urllib.error.HTTPError as e:
#    print(e.code)

'''for line in f:
    f.readline()
    try:
        a = urllib.request.urlopen(line)
        good = a.geturl()
        s.write(good)
        s.write('\n')
    except urllib.error.HTTPError:
        pass'''


for line in f:
    f.readline()
    s.write(line)

f.close()
s.close()

finish = time.localtime()
print('Done. Finish time is: ' + time.asctime(finish))
