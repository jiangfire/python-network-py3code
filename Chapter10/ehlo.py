#SMTP transmission with EHLO -Chapter 10- ehlo.py

import sys, smtplib, socket

if len(sys.argv) < 3:
    print('Syntax: %s fromaddr toaddr [toaddr...]' % sys.argv[0])
    sys.exit(255)

server = 'mx1.qq.com'
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
    code = s.ehlo()[0] #ESMTP的扩展对话， 第一个元素返回的是个数字
    usesesmtp = 1
    if not (200 <= code <= 299):
        usesesmtp = 0
        code = s.helo()[0] #发送这个作为初始的问候，最初的版本 返回的代码在200-299之间的是正常的
        if not (200 <= code <= 299):
            raise SMTPHeloError(code, resp)
    if usesesmtp and s.has_extn('size'):
        print('Mixium message size is', s.esmtp_features['size']) #获得邮件的最大容量
        if len(message) > int(s.esmtp_features['size']):
            print('Message too large; aborting.')
            sys.exit(2)
    s.sendmail(fromaddr, toaddr, message)
except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException) as e:
    print("*** your message may not have been sent!")
    print(e)
    sys.exit(1)
else:
    print("Message successfully sent to %d recipient(s)" % len(toaddr))
    
