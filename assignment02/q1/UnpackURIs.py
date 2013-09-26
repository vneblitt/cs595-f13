import urllib.request
import urllib.error
import os
import time

start = time.localtime()
print('Start time is: ' + time.asctime(start))

f = open('tweetlink.txt', 'r')
s = open('unpackedURLs.txt', 'w')


for line in f:
    print(line)
    try:
        a = urllib.request.urlopen(line)
        good = a.geturl()
        s.write(good)
        print('Kept ' + line + ' as ' + good)
        s.write('\n')
        s.flush()
        os.fsync(s.fileno())
    except:
        print('Throwing out ' + line)
        pass

f.close()
s.close()

finish = time.localtime()
print('Done. Finish time is: ' + time.asctime(finish))
