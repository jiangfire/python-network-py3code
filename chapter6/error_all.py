#Obtain Web Page with Full Error Handling -chapter 6
#error_all.py
#实在不知道百度是什么编码，gzip搞不了
import sys, urllib.request,urllib.error, socket, io, gzip

try:
    req = urllib.request.urlopen(sys.argv[1])
except urllib.error.HTTPError as e:
    print('Error retrieving data:' , e)
    print('Sever Error document follows: \n')
    print(e.read())
    sys.exit(1)
except urllib.error.URLError as e:
    print('Error retrieving data:', e)
    sys.exit(2)

print('Retrieved ', req.geturl())
bytesread = 0

while True:
    try:
        data = req.read(1024)
    except socket.error as e:
        print('Error reading data:', e)
        sys.exit(3)
    if not len(data):
        break
    bytesread += len(data)
    si = io.BytesIO(data) #这是一个类，而不是一个模块
    f = gzip.GzipFile(fileobj = si)
    print(f.read(1024).decode()) #必须设置大小否则就会出现EOFError
if 'Content-Lengeh' in req.info() and req.info()['Content-Lengeh'] != bytesread:
    print('Expected a document of size %d but read %d bytes'  % (fd.info()['Content-Lengeh'], bytesread))
    sys.exit(4)