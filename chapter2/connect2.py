#revised connect example -chapter 2- connect2.py

import socket
print("creating socket...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("done")

print("Looking up port number ....")
port = socket.getservbyname('http', 'tcp')
print('done')

print("Connecting to remote host on port %d ...." % port, s.connect(('www.baidu.com', port)))
print('done')
