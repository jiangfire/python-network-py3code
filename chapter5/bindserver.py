#Echo Server Bounder to Specific Address -chapter 5- bindserver.py
import socket, traceback
host = '127.0.0.1'
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

print('The server is running ...')
while True:
	clientsock, clientaddr = s.accept()
	#process the connection
	print('Got connection from', clientsock.getpeername())
	while True:
		data = clientsock.recv(4096)
		if not len(data):
			break
		clientsock.sendall(data)
	#close the connection
	clientsock.close()