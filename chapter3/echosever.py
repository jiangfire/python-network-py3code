#Echo server -chapter 3- echoserver.py
import socket, traceback

host = '' #bind to all interface
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

while True:
	try:
		clientsock, clientaddr = s.accept()
	except KeyboradInterrupt:
		raise
	except:
		traceback.print_exc()
		continue

	#Process the connection
try:
	print('Got connection from', clientsock.getpeername())
	while True:
		data = clientsock.recv(4096) #只会读取4kb
		if not len(data):
			break
		clientsock.sendall(data) #然后再写
except (KeyboardInterrupt, SystemExit):
	raise
except:
	traceback.print_exc()
#close the connection
try:
	clientsock.close()
except KeyboardInterrupt:
	raise
except:
	traceback.print_exc()

