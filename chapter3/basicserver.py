#base server -chapter 3- basicserver.py
import socket

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
print('waiting for connection....')
s.listen(1)

while True:
    clientsock, clientaddr = s.accept()
    print('got connection from', clientsock.getpeername())
    clientsock.close()