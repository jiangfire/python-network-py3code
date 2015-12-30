#Tradtional Message Generation with Data and Message-ID --chapter 9
#trad-gen-newhdrs.py
#This program requires Python 2.2.2 or above

from email.mime.text import MIMEText
from email import utils

message = """Hello,
This is a test message from chapter 9. I hope you enjoy it!
-- Anonymous"""

msg = MIMEText(message)
msg['To'] = 'reciplient@example.com'
msg['From'] = 'Test Sender <sender@example.com>'
msg['Subject'] = 'Test Message, Chapter 9'
msg['Date'] = utils.formatdate(localtime=1)
msg['Message-ID'] = utils.make_msgid()

print(msg.as_string())