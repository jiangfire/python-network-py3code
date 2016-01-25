#SMTP transmission with TLS -Chapter 10- tls.py
#直接拒绝了
#出错原因
#1. 远程主机不支持TLS
#2. 远程主机在建立适当的TLS session的时候出错
#3. 远程提供的认证不是有效的
import sys, smtplib, socket

if len(sys.argv) < 3:
    print("Syntax: %s server fromaddr toaddr [toaddr...]" % sys.argv[0])
    sys.exit(255)

server = "mx1.qq.com"
fromaddr = sys.argv[1]
toaddr = sys.argv[2:]

message = """To: %s
From:%s
Subject: Test Message from simple.py
Hello, 
This is a test message sent to you from simple.py and smtplib.
""" % (", ".join(toaddr), fromaddr)

try:
    s = smtplib.SMTP(server)
    code = s.ehlo()[0]
    usesesmtp = 1
    if not (200 <= code <= 299):
        usesesmtp = 0
        code = s.helo()[0]
        if not (200 <= code <= 299):
            raise smtplib.SMTPHeloError(code, msg)
    if usesesmtp and s.has_extn('starttls'):
        print("Negotiating TLS...")
        s.starttls()
        code = s.ehlo()[0]
        if not (200 <= code <= 299):
            print("Couldn't Ehlo after STARTTLS")
            sys.exit(5)
            print("Using TLS Connection")
        else:
            print("Server does not suppose TLS; using normal connection.")
        s.sendmail(fromaddr, toaddr, message)
except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException) as e:
    print("*** Your message may not have been sent !")
    print(e)
    sys.exit(1)
else:
    print("Message successfully sent to %d recipent(s)" % len(toaddr))
    