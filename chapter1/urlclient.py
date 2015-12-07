#high-level gopher cilent
import urllib.request, sys
host = input(">")
file = input(">")

f = urllib.request.urlopen("http://%s%s" % (host, file)).read()

print(f.decode())
