#UDP Brocast Server -chapter 5- bcastreceiver.py

import socket, traceback

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))
print("Look up the sender...")

while True:
	try:
		message, address = s.recvfrom(8192)
		print("Got Data From", address)
		#Acknowledge it.
		s.sendto(b"I am Here", address)
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		traceback.ptint_exc()