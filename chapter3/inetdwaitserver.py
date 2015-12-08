#UDP inetd sever for wait -chapter 3- inetwaitsever.py
import socket, time, sys, os

s = socket.fromfd(sys.stdin.fileno(), socket.AF_INET, socket.SOCK_DGRAM)
message, address = s.recvfrom(8192)
localaddr = s.getsockname() #获得本机的地址
s.close()

pid = os.fork()
if pid:
    sys.exit(0)
    
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s2.bind(localaddr)
s2.connect(address)

for i in range(10):
    s2.send(b"reply %d: %s" % (i + 1, message), address)
    time.sleep(2)
    s2.send(b"ok, i am done sending replies.\n")
    