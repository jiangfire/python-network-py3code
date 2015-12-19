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
            #and then start anew on this one.
            self.handle_endtag(tag)
        #Note that we're now processing this tag
        self.taglevels.append(tag)
        if tag in self.handledtags:
            #Only bother saving off the data if it's a tag we handle.
            self.data = ''
            self.processing = tag
            if tag == 'ul':
                print('List started.')