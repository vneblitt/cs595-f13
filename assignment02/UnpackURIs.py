import urllib.request
import urllib.parse
import urllib.error

#a = urllib.request.urlopen('http://goo.gl/LhYg3')

f = open('tweetlink.txt', 'r')
s = open('unpackedURLs.txt', 'w')

#try:
#    print(a.geturl())

#except urllib.error.HTTPError as e:
#    print(e.code)

for line in f:
    f.readline()
    s.write(line)

f.close()
s.close()
