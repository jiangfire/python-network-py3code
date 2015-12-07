#Information example -chapter 2 - connect3.py

import socket

print("Creating socket...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("done")

print("Looking up port number...")
port = socket.getservbyname("http", 'tcp')
print("done")

print("connecting to remote host on port %d...." % port, s.connect(('www.baidu.com', port)))
print("done.")

print("connect from", s.getsockname()) #显示本机的ip地址和端口号
print("connect to", s.getpeername()) #显示远程机器的ip地址和端口号
