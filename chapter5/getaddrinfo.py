#getaddrinfo() display -chapter 5- getaddrinfo.py
#Give a host and port on the commandline

import socket, sys
host, port = sys.argv[1:]

#Look up the given data
results = socket.getaddrinfo(host, port, 0, socket.SOCK_STREAM)

#we may get multiple results bacck, Display each one.
for result in results:
    #Display a separator line to visually segment one result from the next.
    print("-" * 60)

#print whether we got back on Ipv4 or ipv6 result.
if result[0] == socket.AF_INET:
    print("Famliy: AF_INET")
elif result[0] == socket.AF_INET6:
    print("Family:AF_INET6")
else:
    #it's not ipv4 or ipv6, so we don't know about it,just put out its number
    print("Famliy:", result[0])

#Indicate whether it's a stream (TCP) or datagram (UDP) result
if result[1] == socket.SOCK_STREAM:
    print("Socket Type: SOCK_STREAM")
elif result[1] == socket.SOCK_DGRAM:
    print("socket type: SOCK_DGRAM")

#Display the final bits of information from getaddrinfo()
print("Protocol:", result[2])
print("Canoncal Name:", result[3])
print("socket address:", result[4])

