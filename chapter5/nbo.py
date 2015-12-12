# Network Byte Order -chapter 5- nbo.py
import struct, sys

def htons(num):
    return struct.pack('!H', num)

def  hton1(num):
    return struct.pack('!I', num)

def ntohs(data):
    return struct.unpack('!H', data)[0]

def ntoh1(data):
    return struct.unpack('!I', data)[0]

def sendstring(data):
    return (hton1(len(data))+data)

print('Enter the string:')
str1 = input()

print(str(sendstring(str1.encode())))