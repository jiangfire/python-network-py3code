#Obtain Web Page Information With Simple Error Handling -chapter 6
#error_basic.py

import sys, urllib.request, urllib.error
try:    
    req = urllib.request.urlopen('http://' + sys.argv[1])
except urllib.error.URLError as e:
    print('Error retrieving data:', e)
    sys.exit(1)
print('Retrieved', req.geturl())
info = req.info()
for key, value in info.items():
    print('%s : %s' % (key, value))
