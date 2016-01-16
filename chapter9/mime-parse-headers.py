#MIME Header Parsing Chapter 9
#mime-parse-headers.py
#This program requires Python 2.2.2 or above

import sys, email, codecs
from email import header

fd = open('header.txt')
msg = email.message_from_file(fd)
for pheader, value in msg.items():
    headerparts = header.decode_header(value)
    headerval = []
    for part in headerparts:
        data, charset = part
        if charset is None:
            charset = 'ascii'
        dec = codecs.getdecoder(charset)
        enc = codecs.getencoder('iso-8859-1')
        data = enc(dec(data.encode())[0])[0]
        headerval.append(data)
        print(pheader, " ", " ".join(headerval))