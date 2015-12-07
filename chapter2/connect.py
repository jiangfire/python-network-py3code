#Basic Connection Example -chapter 2- coonect.py

import socket

print("Creating socket ....")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #俩参数一个是 ip4 
print("done.")

print("Connect to remote host..")
s.connect(('www.baidu.com', 80)) #国内上不去google，你懂的
print('done')
#python中能将dns解释为ip地址
