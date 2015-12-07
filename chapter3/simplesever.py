import socket
host = '' #bind to all interface
port = 51423

#step 1 create the socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#step 2 set the socket option
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#step 3 bind to a port and interface
s.bind((host, port))

#step 4 listen for connections
s.listen(5)