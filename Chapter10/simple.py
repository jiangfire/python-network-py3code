#Basic SMTP transmission -Chapter 9- simple.py
#发的邮件会发到垃圾邮件箱的
import sys, smtplib

if len(sys.argv) < 4:
    print("Syntax: %s sever fromaddr toaddr [toaddr...]" % sys.argv[0])
    sys.exit(255)

server = sys.argv[1]
fromaddr = sys.argv[2]
toaddr = sys.argv[3:]

message = """To: %s
From: %s
subject:Test Message from simple.py
hello,
This is a test message sent to you from simple.py and smtplib.""" % (', '.join(toaddr), fromaddr)


s = smtplib.SMTP(server)
s.sendmail(fromaddr, toaddr, message)
print("Message successfully sent to %d recipient(s)" % len(toaddr))