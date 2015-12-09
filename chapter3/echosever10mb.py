#Echo client with deadlock -chapter 3- echoclientlock.py
#这个程序会造成死锁
import socket, sys

port = 51423
host = 'localhost'

data = b'x' * 10485760

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

bytewritten = 0
while bytewritten < len(data):
	startpos = bytewritten
	endpos = min(bytewritten + 1024, len(data))
	bytewritten += s.send(data[startpos:endpos]) #系统只发送而不读取，会把buffer充满
	print("wrote %d bytes\r" % bytewritten)
s.shutdown(1)
print('All data sent')
while True:
	buf = s.recv(1024)
	if not len(buf):
		break
	print(buf)