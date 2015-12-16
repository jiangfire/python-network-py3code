#Error-checking gethostbyaddr() example - chapter 4
#gethostbyaddr-paranoid.py
#performs a reverse lookup on the ip address given on command line
#and sanity-checks the result
#这个只能测试IP地址并不能测试域名
#测试IP地址市要双向测试，否则会有假冒的域名
import sys, socket

def getipaddrs(hostname):
	"""Get a list of IP addresses from a given hostname. 
	This is a standard (forward) lookup. """
	result = socket.getaddrinfo(hostname, None, 0, socket.SOCK_STREAM)
	return [x[4][0] for x in result]

def gethostname(ipaddr):
	"""Get a list of IP addresses from a given hostname.
	This is a reverse lookup"""
	return socket.gethostbyaddr(ipaddr)[0]

try:
	#Frist, do the reverse lookup and get the hostname.
	hostname = gethostname(sys.argv[1]) #could raise socket.herror, 也就是找不到域名所对应的ip地址

	#Now, do a forward lookup on the result from the reverse
	#lookup
	ipaddrs = getipaddrs(hostname) #could rasie socket.gaierror
except socket.herror as e:
	print('No host names avaliable for %s;This may be normal' % sys.argv[1])
	sys.exit(0)
except socket.gaierror as e:
	print('Got host name %s, but it could not be forward-resoloved: %s' % (hostname, str(e)))
	sys.exit(1)

#if the forward lookup did not yield the original IP address anywhere
#some one is palying tricks.Explain the situation and exit

if not sys.argv[1] in ipaddrs:
	print("Got hostname %s, but on forward lookup," % hostname)
	print("original Ip %s did not appear in IP address list." % sys.argv[1])
	sys.exit(1)

#Otherwise, show the validated hostname.
print("validated hostname: ", hostname)
