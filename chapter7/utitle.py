#HTML Extended Parse -chapter 7- utiltle.py
import html.entities, html.parser, sys, re

class TitlePaser(html.parser.HTMLParser):
    def __init__(self):
        #The taglevels list keep track of where we are in the tag
        #hierarchy
        self.taglevels = []
        self.handledtags = ['title', 'ul', 'li']
        self.processing = None
        html.parser.HTMLParser.__init__(self)
    def handle_starttag(self, tag, attrs):
        """Called whenever a start tag is encountered."""
        if len(self.taglevels) and self.taglevels[-1] == tag:
            #Processing a previous version of this tag. close it out.
            #and then start a new on this one.
            #看列表中是否有这个标签，有就直接看是否有后标签
            self.handle_endtag(tag)
        #Note that we're now processing this tag
        self.taglevels.append(tag)
        if tag in self.handledtags:
            #Only bother saving off the data if it's a tag we handle.
            self.data = '' #？？？
            self.processing = tag
            if tag == 'ul':
                print('List started.')
    def handle_data(self, data):
        """This function simply records incoming data if we are presentsly
        inside a handled tag.就是对数据的处理"""
        if self.processing: #有标签才会处理
            #This could be slow for large file.For this example,
            #It's a simple way to save off data.
            self.data += data #这个效率低了，应该用stringIO
    def handle_endtag(self, tag):
        if not tag in self.taglevels:
            #we didn't have a start tag for this anyway.just ignore.
            #没有开始标签只有结束标签
            return
        while len(self.taglevels):
        #Obtain the last tag on list and remove it
            starttag = self.taglevels.pop()
            #Finish processing it
            if starttag in self.handledtags:
                self.finishprocessing(starttag)
            #if it's our tag, stop now
            if starttag == tag:
                break
    def cleanse(self):
        """Remove extra witespace from the document."""
        self.data = re.sub('\s+', ' ', self.data)
    
    def finishprocessing(self, tag): 
        self.cleanse() #数据都已处理好了，直接打印就行了
        if tag == 'title' and tag == self.processing: 
            print('Document Title:', self.data)
        elif tag == 'ul':
            print("List Ended.")
        elif tag == 'li' and tag == self.processing:
            print('List item:', self.data)
        
        self.processing = None
        
    def handle_entityref(self, name):
        if name in html.entities:
            self.handle_data(html.entities[name])
        else:
            self.handle_data('&' + name + ';')
    
    def handle_charref(self, name):
        #Vaildata the name
        #处理不可见字符
        try:
            charnum = int(name)
        except ValueError:
            return
        if charnum < 1 or charnum > 255:
            return
        self.handle_data(char(charnum))
    
    def gettitle(self):
        return self.title
    
fd = open(sys.argv[1])
tp = TitlePaser()
tp.feed(fd.read())