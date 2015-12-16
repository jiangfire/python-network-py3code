#Delaying server -chapter 5- delayserver.py
import socket, traceback, time

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

print('The sever has running ...')
while True:
	try:
		clientsock, clentaddr = s.accept()
	except KeyboardInterrupt:
		raise
	except:
		traceback.print_exc()
		continue

	#process the connection
	try:
		print("got connection from", clientsock.getpeername())
		while True:
			try:
				clientsock.sendall(time.asctime().encode() + b"\n")
			except:
				break
			time.sleep(5)
	except KeyboardInterrupt:
		raise
	except:
		traceback.print_exc()