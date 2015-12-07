#get list of avaliable socket option --chapter 3-- socketopts.py
import socket
solist = [x for x in dir(socket) if x.startswith('SO_')]
solist.sort()
for x in solist:
    print(x)