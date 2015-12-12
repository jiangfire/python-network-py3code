#Basic DNS library example -chapter 4 DNS-basic.py
import sys, DNS

query = sys.argv[1]
DNS.DiscoverNameServers()

regobj = DNS.Request()

answerobj = regobj.req(name = query, qtype = DNS.Type.ANY)
if not len(answerobj.answers):
	print('Not Found')
for item in answerobj.answers:
	print("%-5s %s" % (item['typename'], item['data']))

#A record 给出一个主机名ip的地址
#Mx邮件
#ns为一个域定义名称服务器