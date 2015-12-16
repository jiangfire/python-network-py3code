#Nonblocking I/O with select() -chapter 5- selectclient.py
import socket, sys, select

host = ''
port = 51423

spinsize = 10
spinpos = 0
spindir = 1

def spin():
	global spinsize, spinpos, spindir
	spinstr = '.' * spinpos + '|' + '.'*(spinsize - spinpos - 1)
	print("\r" + spinstr + ' ')

	spinpos += spindir
	if spinpos < 0:
		spindir = 1
		spinpos = 1
	elif spinpos >= spinsize:
		spinpos -= 2
		spindir = -1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while True:
	infds, outfds, errfds = select.select([s], [], [s], 0.05)
	if len(infds):
		#Normally, one would using something like "for fd infds" here.
		#We don't bother since there there will only ever be single file
		#descript there
		data = s.recv(4096)
		if not len(data):
			print('\rRemote and closed connection; exiting.')
			break
		#Only one item in here -- if there's anything, it's for us
		print('\rRevevcing....')
