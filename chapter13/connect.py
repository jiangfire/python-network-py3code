#!/usr/bin/env python3
#Basic connection -chpater 13- connect.py
#step 1 FTP客户端通过连接FTP服务器的一个端口建立一个指令通道连接
#step 2 客户端进行认证
#step 3 客户端转到服务器上合适的目录
#step 4 客户端在一个新端口上建立数据信道开始侦听，同时通知服务器使用了哪个端口
#step 5 服务器连接到客户端申请的端口
#step 6 文件开始被传输，传输结束后，数据信道被关闭
from ftplib import FTP

f = FTP('ftp.ibiblio.org')
print("Welcome:", f.getwelcome())
f.login()

print("CWD:", f.pwd())
f.quit()