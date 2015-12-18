#Submit Post Data -chapter 6- submit_post.py
import sys, urllib.parse, urllib.request

zipcode = sys.argv[1]
url = 'http://www.wunderground.com/cgi-bin/findweather/getForecast'
data = urllib.parse.urlencode([('query', zipcode)])
req = urllib.request.urlopen(url,data.encode()) #data 属性必须是bytes
while True:
    data = req.read(1024)
    if not len(data):
        break
    print(data.decode('gbk'))