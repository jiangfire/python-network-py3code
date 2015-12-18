#Obtain Web Page information with error document handling -chapter 6
#error_doc.py

import sys, urllib.request, urllib.error

try:
    req = urllib.request.urlopen(sys.argv[1])
except urllib.error.HTTPError as e:
    print('Error retrieving data: ', e)
    print('Server error document follows: \n')
    print(e.read())
    sys.exit(1)
except urllib.error.URLError as e:
    print('Error retrieving data:', e)
    sys.exit(2)

print('Retrieved', req.geturl())
info = req.info()
for key, value in info.items():
    print("%s : %s" % (key, value))