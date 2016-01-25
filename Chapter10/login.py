#SMTP transmission with authentication -chapter 10- login.py
#SMTP会话可以使用SSL/TLS加密和认证
#在SMTP中使用TLS过程
#1.像通常那样建立SMTP对象
#2.发送EHLO指令。如果远程主机不支持EHLO，他将不支持TLS
#3.检查s.has_extn(), 看他是否提供starttls。如果不提供，远程主机不支持TLS，邮件需要用
#正常方式发送（或产生一个错误）
#4.调用starttls()来初始化加密通道
#5.再次调用ehlo（）,这一次他是加密的了
#6.发送邮件
import sys, smtplib, socket
from getpass import getpass

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

print("Enter username: ")
username = input().strip()
password = getpass()

try:
    s = smtplib.SMTP()
    try:
        s.login(username, password)
    except smtplib.SMTPAuthenticationError as e:
        print("Authentication failed:", e)
        sys.exit(1)
    s.sendmail(message)
except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException) as e:
    print("*** Your message may not have been sent!")
    print(e)
    sys.exit(2)
else:
    print("Message successfully sent to %d recipient(s)" % len(toaddr))
    
#这个程序无法发送，提示please run connect() frist