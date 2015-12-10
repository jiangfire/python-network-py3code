#Basic gethostbyaddr() example -chapter 4- gethostbyaddr-basic.py
#This program performs a reverse lookup on the ip address given
#on the command line
#只反向查找会被伪造dns
import sys, socket
try:
	#perform the lookup
	result = socket.gethostbyaddr(sys.argv[1])

	#Display the look-up hostname
	print('Primary hostname:')
	print(result[0]) #这里面放的是域名
	#display the list of avaliable address that is also returned
	print('\nAddresd:')
	for item in result[2]:
		print(" " + item)
except socket.herror as e:
	print('could not look up name:', e)