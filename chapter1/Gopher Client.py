import socket, sys

port = 70
host = input("输入地址：")
filename = input("文件名：")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try：
    s.connect((host, port))
except socket.gaierror, e:
    print("error connectint to sever %s" % e)
    sys.exit(1)
s.sendall(str.encode(filename) + b"\r\n") #传送只能是byte类型的

while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    print(buf.decode("utf-8"))  #打印的只能是utf-8类型
