#Obtain Web Page -Chapter 6- dump_page.py
import sys, urllib.request
#python3 中已将urllib2拆封为urllib.request 和 urllib.error
rd = urllib.request.urlopen("http://" + sys.argv[1]) #要加上http:// 否则会出现无法识别type
while True:
	data = rd.read(1024)
	if not len(data):
		break
	print(data.decode())