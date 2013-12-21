import re
from urllib import urlopen
webpage = urlopen('http://timesofindia.feedsportal.com/c/33039/f/533965/index.rss').read()
findTitle = re.compile('<title>(.+?)</title>')
findPatTitle = re.findall(findTitle,webpage)
findLink = re.compile('<guid isPermaLink="false">(.+?)</guid>')
findPatLink = re.findall(findLink,webpage)
findNews = re.compile('<div class="Normal">(.+?)</div>')
for i in range(2,27):
	print findPatTitle[i]
	news = urlopen(findPatLink[i-2]).read()
	findPatNews = re.findall(findNews,news)
	try:
		findPatNews = re.sub('<.+?>','',findPatNews[0])
	except:
		print "Could not retrieve data"
	print findPatNews
	print "\n"
