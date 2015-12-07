#UDP connectionless example -chapter2- udptime.py

import socket, sys, struct, time
hostname = b'time.nist.gov'
#port = 37
#host = socket.gethostbyname(hostname)
host = ''
port = 51423
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b'', (host, port))

print('looking for replies; press Ctrl-C to stop')
buf = s.recvfrom(2048)[0]
if len(buf) != 4:
    print(b"Wrong size reply %d:%s" % (len(buf), buf.encode()))
    sys.exit(1)

secs = struct.unpack('!I', buf)[0]
secs -= 2208988800
print(time.ctime(int(secs)))
