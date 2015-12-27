import xmlrpc.client

sever = xmlrpc.client.ServerProxy('http://localhost:51423')

words = sever.sayHello()

print("result:" + words)