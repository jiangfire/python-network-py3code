#error handling example with shutdown -chapter 2- shutdown.py
#能够察觉出来就是多设置几个错误处理
import socket, sys, time

host = sys.argv[1]
textport = sys.argv[2]
filename = sys.argv[3]

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print("strange error creating socket: %s" % e) #建立一个socket对象才能进行联网
    sys.exit(1)

#try parsing it as a numberic port number.

try:
    port = int(textport)
except socket.error as e:
    print("couldn't find your port: %s" % e) #不在自动找端口了
    sys.exit(1)

try:
    s.connect((host, port)) #链接
except socket.gaierror as e:
    print("connection error: %s" % e)
    sys.exit(1)

print("sleep...")
time.sleep(10)
print('continuting')

try:
    s.sendall(b'GET %s HTTP/1.0\r\n\r\n' % filename.encode()) #寄出一个文件
except socket.error as e:
    print('error sending data (detected by shut down): %s' % e)
    sys.exit(1)

while True:
    try:
        buf = s.recv(2048) #看来是接收一个长为2048的数据
    except socket.error as e:
        print('error receiving data: %s' % e)
        sys.exit(1)
    if not len(buf):
        break
    print(buf)
