#Submit GET Data -chapter 6- submit_get.py
import sys, urllib.parse, urllib.request
def addGETdata(url, data):
    """Adds data to url. Data should be a list or tuple
    consisting or 2-item lists or tuples of the form:(key, value)
    
    Items that have no key should have key set to None.
    A Given key may may occur more than once."""
    
    return url + '?' + urllib.parse.urlencode(data)
zipcode = sys.argv[1]
url = addGETdata('http://www.wunderground.com/cgi-bin/findweather/getForecast', [('query', zipcode)])

print('Using URL:', url)
req = urllib.request.urlopen(url)
while True:
    data = req.read(1024)
    if not len(data):
        break
    print(data.decode('gbk'))