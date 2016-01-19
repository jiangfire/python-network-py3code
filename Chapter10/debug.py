#socket.gaierror, 寻找地址时出现的错误
#socket.error, 普通的I/O和通讯问题
#socket.herror, 其他地址错误
#smtlib.SMTPException或它的一个子类，是SMTP会话问题
#smtlib提供了一个发现隐藏在表面之下的运行情况。调用smtpobj.set_debuglevel(1)
#可跟踪所有问题
#mx1.qq.com 是默认qq发送邮件的地址
#SMTP transmission with debugging - Chapter 10- debug.py
import sys, smtplib, socket

if len(sys.argv) < 4:
    print('Syntax: %s server fromaddr toaddr [toaddr...]' % sys.argv[0])
    sys.exit(255)

server = sys.argv[1]
fromaddr = sys.argv[2]
toaddr = sys.argv[3:]

message  = """To: %s
From: %s
Subject: Test Message from simple.py

Hello,
This is a test message sent to you from simple.py and smtlib.
""" % (', '.join(toaddr), fromaddr)

try:
    s = smtplib.SMTP(server)
    s.set_debuglevel(1)
    s.sendmail(fromaddr, toaddr, message)
except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException) as e:
    print('*** your message may not have been sent!')
    print(e)
    sys.exit(1)
else:
    print('Message successfully sent to %d recipient(s)' % len(toaddr))

#现在的大多数服务器都有两个，第一个接受了不代表第二个也接受了