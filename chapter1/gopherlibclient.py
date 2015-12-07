#High-Level Gopher CLient - chapter 1 -gopherlivclient.py
#这个模块删除了，大家看看就好 在python3中
import gopherlib, sys

host = input("请输入地址：")
file = input("请输入文件地址：")

f = gopherlib.send_selector(file.encode(), host.encode())
for line in f.readlines():
    print(line)
