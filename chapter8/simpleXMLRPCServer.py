import xmlrpc.server

class MyObject:
    def sayHello(self):
        return 'hello xmlrpc'

obj = MyObject()
sever = xmlrpc.server.SimpleXMLRPCServer(('localhost', 51423))
sever.register_instance(obj)

print("Listen on port 51423")

sever.serve_forever()