#Basic getaddrinfo() list example -chapter 4- getaddrinfo-list.py

import sys, socket

#obtain result for socket.SOCK_STREAM(tcp) only, and put a list
#of them into the 'result' varible.

result = socket.getaddrinfo(sys.argv[1], None, 0, socket.SOCK_STREAM)

counter = 0
for item in result:
	#print out the address tuple for each item
	print('%-2d : %s' % (counter, item[4]))
	counter += 1