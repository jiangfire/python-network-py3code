#XML-RPC Basic Client -Chapter 8- xmlrpcbasic.py
#很不幸这个服务已经停止了
import xmlrpc.client

url = 'http://www.oreillynet.com/meerkat/xml-rpc/sever.php'
s = xmlrpc.client.ServerProxy(url)
a = s.listMethods()
print(a)