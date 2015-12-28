#Tradtion Message Generation, Simple --chapter 9
#trad_gen_simple.py
#This program requires Python 2.2.2 or above

from email.mime.text import MIMEText

message = """Hello,
This is a test message from Chapter 9. I hope you enjoy it!
-- Anonymous"""

msg = MIMEText(message)
msg['To'] = 'example@example.com'
msg['From'] = 'Test Sender <sender@Example.com>'
msg['Subject'] = 'Test Message, Chapter 9'

print(msg.as_string())