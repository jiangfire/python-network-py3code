#MIME attachment generation -Chapter 9- mime-gen-basic.py
#This program requires Python 2.2.2 or above

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import utils, encoders
import mimetypes, sys

def attachment(filename):
    fd = open(filename, 'rb')
    mimetype, mimeencoding = mimetypes.guess_type(filename)
    if mimeencoding or (mimetype is None):
        mimetype = 'application/octet-stream'
    maintype, subtype = mimetype.split('/')
    if maintype == 'text':        
        retval = MIMEText(fd.read().decode(), _subtype=subtype)
    else:
        retval = MIMEBase(maintype, subtype)
        retval.set_payload(fd.read())
        encoders.encode_base64(retval)
    retval.add_header('Content-Disposition', 'attachment', filename = filename)
    fd.close()
    return retval

message = """Hello,
This is a test message from Chapter 9. I hope you enjoy it!
-- Anonymous"""

msg = MIMEMultipart()
msg['To'] = 'recipient@example.com'
msg['From'] = 'Test Sender <sender@example.com>'
msg['Subject'] = 'Test Message, Chapter 9'
msg['Date'] = utils.formatdate(localtime=1)
msg['Message-ID'] = utils.make_msgid()

body = MIMEText(message, _subtype='plain')
msg.attach(body)
for filename in sys.argv[1:]:
    msg.attach(attachment(filename))
print(msg.as_string())
fd = open(file='message.txt', mode='w')
fd.write(msg.as_string())
fd.close()