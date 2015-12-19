import html.parser, sys
class TitleParser(html.parser.HTMLParser):
    def __init__(self):
        self.title = ''
        self.readingtitle = False
        html.parser.HTMLParser.__init__(self)
    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.readingtitle = True
    def handle_data(self, data):
        if self.readingtitle:
            #Ordinarilly, this is slow and a bad practice, but
            #We can get away with it because a title is usually small
            #and simple
            self.title += data
    def handle_endtag(self, tag):
        if tag == 'title':
            self.readingtitle = False
    def gettitle(self):
        return self.title
    def handle_charref(self, name):
        #validate the name
        try:
            charnum = int(name)
        except ValueError:
            return
        if charnum < 1 or charnum > 255:
            return
        self.handle_data(chr(charnum))

fd = open(sys.argv[1])
tp = TitleParser()
tp.feed(fd.read())
print('Title is ', tp.gettitle().encode())