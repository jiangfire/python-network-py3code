#Connect Example with ipv6 Awareness -chapter 5-ipv6connect.py
#ipv6 如果没支持就不会得到结果
import socket, sys

def getaddrinfo_pref(host, port, socketype, famliypreference = socket.AF_INET):
    """Given a host, port, and socketype(usually socket.SOCK_STREAM or
    socket.SOCK_DGRAM), looks up information with ipv4 and ipv6. If 
    information is found corresponding to the famliyperference, it is
    returned. otherwise, any information found is returned.The family
    prencence defaults to ipv4(socket.AF_INET) but you could also set 
    it to socket.AF_INET6 for ipv6.

    The return value is the appropriate tuple returned from
    socket.getaddrinfo()"""
    results = socket.getaddrinfo(host, port, 0, socketype)
    for result in results:
        if result[0] == famliypreference:
            return result
        return results[0]

host = sys.argv[1]
port = 'http'

c = getaddrinfo_pref(host, port, socket.SOCK_STREAM)
print("Connecting to ", c[4])
s = socket.socket(c[0], c[1])
s.connect(c[4])
s.sendall(b"HEAD / HTTP/1.0\n\n")

while True:
    buf = s.recv(4096)
    if not len(buf):
        break
    print(buf.decode())
