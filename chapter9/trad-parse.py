#Tradtional Message Parsing --Chapter 9
#trad_parse.py
#This program requires Python 2.2.2 or above

import sys, email

fd = open('message.txt', 'r')
msg = email.message_from_file(fd)
fd.close()
print(" *** Headers in message: ")
for header, value in msg.items():
    print(header + ": " + value)
    
if msg.is_multipart():
    print("This program cannot handle MIME multipart messages; exiting.")
    sys.exit()
    
print('-' * 78)
if 'suject' in msg:
    print("Subject: ", msg['subject'])
    print('-' * 78)

print('Message Body: ')
print()
print(msg.get_payload())