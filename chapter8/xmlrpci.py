#XML-RPC Introspection Client -Chapter 8- xmlrpci.py
#这方法都要自己提供，有兴趣的可以看文档
import xmlrpc.client, sys

url = 'http://localhost:51423'
s = xmlrpc.client.ServerProxy(url)

print('Gathering avilable methods...')
methods = s.listMethods()

while True:
    print('\n\nAvailable Method:')
    for i in range(len(methods)):
        print('%2d: %s' % (i + 1, methods[i]))
    selection = input('Select one(q to quit):')
    if selection == 'q':
        break
    item = int(selection) - 1
    print("Details for %s\n" % methods[item])
    for sig in s.methodSignature(methods[item]):
        print("Args: %s; Return: %s" % (", ".join(sig[1:]), sig[0]))
        print("Help：", s.methodHelp(methods[item]))
        