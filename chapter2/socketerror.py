#error handling example -chapter 2- socketerror.py
import socket, sys
host = input("请输入地址：")
textport = input("..")
filename = input("..")

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print("Strange error creating socket: %s" % e)
    sys.exit(1)

#try parsing it as a numeric port num
try:
    port = int(textport)
except ValueError:
    #that didn't work, so it's probably a protocol name
    #look it up instead
    try:
        port = socket.getservbyname(textport, 'tcp')
    except socket.error as e:
        print("couldn't find your port: %s" % e)
        sys.exit(1)
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print('connection error: %s' % e)
        sys.exit(1)

    while True:
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print("error reciving date: %s" % e)
            sys.exit(1)

            if not len(buf):
            break
        print(buf)
            
