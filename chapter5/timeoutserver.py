#Echo Server with Timeouts -chapter 5- timeoutsever.py
import socket, traceback

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

while True:
    try:
        clientsock, clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
    clientsock.settimeout(5)

    #Process the connection
    try:
        print("Got connection from", clientsock.getpeername())
        while True:
            data = clientsock.recv(4096)
            if not len(data):
                break
            clientsock.sendall(data)
    except (KeyboardInterrupt, SystemExit):
        raise
    except socket.timeout:
        pass
    except:
        traceback.print_exc()
