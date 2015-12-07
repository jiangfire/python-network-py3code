import socket, sys
port = 70
host = input("请输入地址：")
filename = input("请输入：")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
fd = s.makefile('rwb', 0)

fd.write(filename.encode("utf-8") + '\r\n'.encode('utf-8'))

for line in fd.readlines():
    print(line.decode('utf-8'))
