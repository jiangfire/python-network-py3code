#Sever With Error hanling -chapter 3- errorserver.py
import socket, traceback

host = '' #bind to all interfface
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)
print('The is runing...')
while True:
    try:
        clientsock, clientaddr = s.accept()
    except KeyboardInterrupt:
        raise 
    except:
        traceback.print_exc()
        continue
    #process the connection
    try:
        print('Got the connection from', clientsock.getpeername())
        #process the request here
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
    #close the connection
    try:
        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
    
        
    