#basic inted server -chapter 3- inetdserver.py
#这部分windows并没有提供，如果是windows的同学就不要试了
#我这电脑只有windows 所以后面的例子都没试
import sys

print('welcome.')
print('please enter a string:')
sys.stdout.flush()
line = input().strip()
print('you enter %d characters.' % len(line))