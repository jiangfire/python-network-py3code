#socket-based inetd sever -chapter 3 -inetdsocket.py

import sys, socket, time
#inetd程序可以知道请求的是哪个服务器程序
s = socket.fromfd(sys.stdin.fileno(), socket.AF_INET, socket.SOCK_STREAM)
#socket对象是inetd 传过来的
s.sendall(b"welcome.\n")
s.sendall(b"According to our records, you are connection from %s.\n" % str(s.getpeername()).decode())
s.sendall(b"The local time is %s.\n" % time.asctime())