#simple sever chapter -simple sever.py
import socket
host = ''
port = 51432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

print("sever is runing on port %d;press ctrl-c to terminate." % port)

while True:
    clientsock, clientaddr = s.accept()
    clientfile = clientsock.makefile('rwb', 0)
    clientfile.write(b"Welcome," + str(clientaddr).encode() + b"\n")
    line = clientfile.readline().strip()
    clientfile.write(b"YOU enter %d characters.\n" % len(line)) #记得要使用byte
    clientfile.close()
    clientsock.close()
    
