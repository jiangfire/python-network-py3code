#MIME message generation with 8-bits header -Chapter 9
#mime-headers.py
#This program requires Python 2.2.2 or above

from email.mime.text import MIMEText
from email.header import Header
from email import utils

message = """Hello, 
This is a test message from chapter 9. I hope you enjoy it!
-- Anonymous"""

msg = MIMEText(message)
msg['To'] = 'recipient@example.com'
fromhdr = Header("Michael M\xfcller", 'iso-8859-1')
fromhdr.append('<mmueller@example.com>', 'ascii')
msg['From'] = fromhdr
msg['Subject'] = Header('Test Message, Chapter 10')
msg['Date'] = utils.formatdate(localtime=1)
msg['Message-ID'] = utils.make_msgid()
print(msg.as_string())