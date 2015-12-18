#Obtain Web Page Information With Authentication -chapter 6
#Dump_info_auth.py
#这个网站已经不需要密码了
import sys, urllib.request, getpass

########################################################################
class TermainalPassword(urllib.request.HTTPPasswordMgr):        
    def find_user_password(self, realm, authuri):
        retval = urllib.request.HTTPPasswordMgr.find_user_password(self, realm, authuri)
        
        if retval[0] == None and retval[1] == None:
            #did not find it in stored values; prompt user.
            print('Login required for %s as %s\n' % (realm, authuri))
            username = ''
            password = ''
            return (username, password)
        else:
            return retval
        
    
req = urllib.request.build_opener(urllib.request.HTTPBasicAuthHandler(TermainalPassword()))
fd = req.open(input('输入网址：'))
print("Retrieved", fd.geturl())
info = fd.info()
for key, value in info.items():
    print('%s = %s' % (key, value))