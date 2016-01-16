from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import utils, encoders
import mimetypes, sys

def genpart(data, contenttype):
    maintype, subtype = contenttype.split('/')
    if maintype == 'text':
        retval = MIMEText(data, _subtype=subtype)
    else:
        retval = MIMEBase(maintype, subtype)
        retval.set_payload(data)
        encoders.encode_base64(retval)
    return retval

def attachment(filename):
    fd = open(filename, 'rb')
    mimetype, mimeencoding = mimetypes.guess_type(filename)
    if mimeencoding or (mimetype is None):
        mimetype = 'application/octet-stream'
    retval = genpart(fd.read(), mimetype)
    retval.add_header('Content-Disposition', 'attachment', filename=filename)
    fd.close()
    return retval

message = """Hello,
This is a *great* test message from Chapter 9, I hope you enjoy it!
--Anonymous"""
messagehtml = """Hello, <p>This is a <b>greay</b> test message from chapter 9. I hope you enjoy it!
--<i>anonymous</i>"""

msg = MIMEMultipart()
msg['To'] = 'recipiet@example.com'
msg['From'] = 'Test Sender <sender@example.com>'
msg['Subject'] = 'Test Message, Chapter 9'
msg['Data'] = utils.formatdate(localtime = 1)
msg['Mssage-ID'] = utils.make_msgid()

body = MIMEMultipart('alternative')
body.attach(genpart(message, 'test/plain'))
body.attach(genpart(messagehtml, 'text/html'))
msg.attach(body)

for filename in sys.argv[1:]:
    msg.attach(attachment(filename))
print(msg.as_string())