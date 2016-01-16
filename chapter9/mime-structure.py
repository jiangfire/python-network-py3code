#MIME Message Parsing -Chapter 9- mime-structure.py
#This program requires Python 2.2.2 or above

import sys, email

def printmsg(msg, level=0):
    l = "|" * level
    l2 = l + "|"
    print(l + 'Message Headers:')
    for header, value in msg.items():
        print(l2, header + ':', value)
    if msg.is_multipart():
        for item in msg.get_payload():
            printmsg(item, level + 1)

fd = open(file='message.txt', mode='r')
msg = email.message_from_string(fd.read())
fd.close()
printmsg(msg)