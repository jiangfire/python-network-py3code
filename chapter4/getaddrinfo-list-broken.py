#Basic getaddrinfo() not quite right list example -chapter 4-
#getaddrinfo-list-broken.py
#Takes a hostname on command line and print all resulting
#matches for it.Broken; a given name may occur multiple times.
#getaddrinfo()会根据根据每种他支持的协议产生一个结果
import sys, socket

#put the list of result into the 'result' variable

result = socket.getaddrinfo(sys.argv[1], None) #第一个是域名， 第二个是端口

counter = 0
for item in result:
	#print out the address tuple for each item
	print('%-2d: %s' % (counter, item[4]))
	counter += 1
