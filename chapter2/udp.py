#UDP example -chapter 2- udp.py
import socket, sys

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGERM) #后面就改了个协议，其余的基本不变
try:
    port = int(textport)
except ValueError:
    port = socket.getservbyname(textport, 'tcp')

s.connect((host, port))
print('enter data to transmit')
data = input()
s.sendall(data)
print('looking for replies; press ctrl-c to stop')
while True:
    buf = recv(2048)
    if not len(buf):
        break
    print(buf)
