#error handling example with shutdown and file-like objects -chapter-2
#shutdownfile.py

import socket, sys, time

host = sys.argv[1]
textport = sys.argv[2]
filename = sys.argv[3]

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print('strange error creating socket: %s' % e)
    sys.exit(1)

#try parsing it as numeric port num

try:
    port = int(textport)
except ValueError:
    #that didn't work . look it up instead
    try:
        port = socket.getservbyname(textport, 'tcp')
    except socket.error as e:
        print("can't find your port: %s" % e)
        sys.exit(1)

try:
    s.connect((host, port))
except socket.gaierror as e:
    print('address-related error connecting to serve: %s' % e)
    sys.exit(1)
fd = s.makefile('rwb', 0) #最好不要指定缓冲器，socket其实是一个文件对象，可读可写

print('sleeping')
time.sleep(5)
print('continuing.')

try:
    fd.write(b'GET %s HTTP/1.0\r\n\r\n' % filename.encode())
except socket.error as e:
    print('error sending data:%s' % e)
    sys.exit(1)

try:
    s.shutdown(1)
    s.close()
except socket.error as e:
    print("error sending data (detected by shutdown): %s" % e)
    sys.exit(1)
while True:
    try:
        buf = fd.read(2048) 
    except socket.error as e:
        sys.exit(1)
        if not len(buf):
            break
        print(buf)
    
