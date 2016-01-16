#MIME part decoding -Chapter 9- mime_decoding.py
#this program requires python 2.2.2 or above

import sys, email

counter = 0
parts = []

def printmsg(msg, level = 0):
    global counter
    l = "l " * level
    ls = l + '*'
    l2 = l + "|"
    if msg.is_multipart():
        print(l + "Found multipart:")
        for item in msg.get_payload():
            printmsg(item, level + 1)
    else:
        disp = ['%d. Decode part' % (counter+1)] #记得加括号否则会出现Type error 是先代换后求值
        if 'content-type' in msg:
            disp.append(msg['content-type'])
        if 'content-disposition' in msg:
            disp.append(msg['content-disposition'])
        print(l + ', '.join(disp))
        counter += 1
        parts.append(msg)

inputfd = open(sys.argv[1])
msg = email.message_from_file(inputfd)
printmsg(msg)

while 1:
    print('Select part number to decode or q to quit:')
    part = sys.stdin.readline().strip()
    if part == 'q':
        sys.exit(0)
    try:
        part = int(part)
        msg = parts[part - 1]
    except:
        print("Invaild selection.")
        continue
    print("Select file to write to:")
    filename = sys.stdin.readline().strip()
    try:
        fd = open(filename, 'wb')
    except:
        print("Invaild filename.")
        continue
    fd.write(msg.get_payload(decode=1))
            

