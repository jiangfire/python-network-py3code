#Basic gethostaddr() example -chapter 4- environment.py

import sys, socket

def getipaddrs(hostname):
	"""Given a hostname, perform a standard (forward) lookup and
	return a list of ip addresses for that host."""
	result = socket.getaddrinfo(hostname, None, 0, socket.SOCK_STREAM)
	return [x[4][0] for x in result]

#Calling gethostname() returns the name of local machine 获得的是本机的IP地址
hostname = socket.gethostname()
print("Host name:", hostname)

#Try to get the fully quaified name
print("Fully-qualified name:", socket.getfqdn(hostname)) #获得的是被辨识的地址

try:
	print("IP addresses:", ", ".join(getipaddrs(hostname)))
except socket.gaierror as e:
	print("Couldn't get ip addresses:", e)