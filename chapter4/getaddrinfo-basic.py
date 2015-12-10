#Basic getaddrinfo() basic example -chapter 4- getaddrinfo.py
import sys, socket
result = socket.getaddrinfo(sys.argv[1], None)
print(result[0][4])