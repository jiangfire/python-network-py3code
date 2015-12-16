#Obtain a web page information -chapter 6- dump_info.py
import sys, urllib.request

req = urllib.request.urlopen('http://' + sys.argv[1])
print('Retrieved', req.geturl())
info = req.info()
for key, value in info.items():
	print("%s = %s" % (key, value))