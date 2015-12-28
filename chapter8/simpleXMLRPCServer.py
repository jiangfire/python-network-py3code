import xmlrpc.server
#为了能让她使用我就自己搭建了个服务器
class MyObject:
    def sayHello(self):
        return 'hello xmlrpc'
    def sayNihao(self):
        return "NiHao"
    def listMethods(self):
        return ['sayNihao', 'sayHello']
    def methodSignature(self, text):
        if text == 'sayHello':
            return self.sayHello()
        elif text == 'sayNihao':
            return self.sayNihao()
        

obj = MyObject()
sever = xmlrpc.server.SimpleXMLRPCServer(('localhost', 51423))
sever.register_instance(obj)

print("Listen on port 51423")

sever.serve_forever()