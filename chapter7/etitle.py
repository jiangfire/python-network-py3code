#Html tilte retriever with entity support -chapter 7- etitle.py
#python3 中已移除entitydefs这个模块
#python3 好像不用处理
import html.parser, sys, html.entities

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
            self.title += data
    def handle_endtag(self, tag):
        if tag == 'title':
            self.readingtitle = False
    def handle_entityref(self, name):
        if name in html.entities:
            self.handle_data(html.entities[name])
        else:
            self.handle_data('&' + name + ';')
    def gettitle(self):
        return self.title
fd = open(sys.argv[1])
tp = TitleParser()
tp.feed(fd.read())
print('Title is:', tp.gettitle())