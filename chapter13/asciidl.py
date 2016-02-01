#ASCII download -Chapter 13- asciidl.py
#Download README from remote and writes it to disk

from ftplib import FTP

def writeline(data):
    fd.write(data + "\n")

f = FTP('ftp.kernel.org')
f.login()

f.cwd('/pub/linux/kernel') #在远处的系统上转换目录
fd = open('README', 'wt') #第一个参数是指定一个在远程系统上执行的命令，第二个是运行的方法
f.retrlines('RETR README', writeline)
fd.close()
f.quit()