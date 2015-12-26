#XML-RPC Basic Client -Chapter 8- xmlrpcbasic.py

import xmlrpc

url = 'http://www.oreillynet.com/meerkat/xml-rpc/sever.php'
s = xmlrpc.client.ServerProxy(url)
catdata = s.meerkat.getCategories()
