#udp inetd server -chapter 3- intedudpserver.py
import socket, time, sys
s = socket.fromfd(sys.stdin.fileno(), socket.AF_INET, socket.SOCK_DGRAM)
message, address = s.recvfrom(8192)
s.connect(address)
for i in range(10):
    s.send('Reply %d: %s' % (i + 1, message))
    time.sleep(2)
    
s.send("ok, i'm done sending replies.\n")
