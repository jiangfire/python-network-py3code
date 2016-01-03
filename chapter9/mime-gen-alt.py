#!/usr/bin/env python3
#MIME alternative generation -Chapter 9- mime-gen-alt.py
#This program requires Python 2.2.2 or above
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart, MIMEBase
from email import utils, encoders
import mimetypes, sys

def alternative(data, contenttype):
    maintype, subtype = contenttype.split('/')
    if maintype == 'text':
        retival = MIMEText(data, _subtype=subtype)
    else:
        retival = MIMEBase(maintype, subtype)
        retival.set_payload(data)
        encoders.encode_base64(retival)
    return retival

messagetext = """Hello,
This is a *great* test message from chapter 9. I hope you enjoy it!
-- Anonymous"""
messagehtml = """Hello, <p>
This is a <b>great</b> test message from Chapter 9. I hope you enjoy it!</p>
-- <i>Anonymous</i>"""

msg = MIMEMultipart('alternative')
msg['TO'] = 'recipient@example.com'
msg['From'] = 'Test Sender <sender@example.com>'
msg['Subject'] = 'Test Message, Chapter 9'
msg['Date'] = utils.formatdate(localtime=1)
msg['Message-ID'] = utils.make_msgid()
msg.attach(alternative(messagetext, 'text/plain'))
msg.attach(alternative(messagehtml, 'text/html'))
print(msg.as_bytes().decode())