#Broadcast sender -chapter 5- bcastsender.py

import socket, sys
dest = ('<broadcast>', 51423)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.sendto(b"Hello, ", dest)

print("Looking for repiles; press Ctrl-C to shut up.")
while True:
	(buf, address) = s.recvfrom(2048)
	if not len(buf):
		break
	print('Received from %s: %s' % (address, buf))