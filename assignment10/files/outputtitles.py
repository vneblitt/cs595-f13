import feedparser

d = feedparser.parse('http://gimmelego.blogspot.com/feeds/posts/default?max-results=100')

for item in d.entries:
	print item.title
