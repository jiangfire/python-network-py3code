#Weather Parser -chapter 7- weather.py
#很可惜这个例子已经不能用了，官网不再搞表格了
from html.entities import entitydefs
from html.parser import HTMLParser
import sys, re, urllib.request

#Declare a list of interesting tables
interesting = ['Day Forecast for ZIP']

class WeatherParser(HTMLParser):
    """Class to parse weather data from www.wunderground.com"""
    def __init__(self):
        #Storage for parse tree
        self.taglevels = []
        #List of tags that are interesting
        self.handletags = ['title', 'table', 'tr', 'td', 'th']
        
        #Set to the interesting tag currently being processed
        self.processing = None
        
        #True if currently processing an interesting table 识别表格
        self.interestingtable = 0
        
        #If processing an interesting table, holds cells in current row 处理表格行
        self.row = []
        
        #Initialize base class.
        HTMLParser.__init__(self)
    def handle_starttag(self, tag, attrs):
        """Called by base class to handle start tags."""
        if len(self.taglevels) and self.taglevels[-1] == tag:
            #Processing a previous version of this tag. Close it out
            #and the start a new this one 处理嵌套列表
            self.handle_endtag(tag)
        self.taglevels.append(tag)
        if tag == 'br':
            #Add a special newline token to the stream
            self.handle_data('<NEWLINE>')
        elif tag in self.handletags:
            #Strat processing an interesting tag.
            self.data = ''
            self.processing = tag #表示处理的标签
    def handle_data(self, data):
        """Called by both HTMLParser and methods in WeatherParser to handle
        plain data."""
        if self.processing:
            self.data += data
    def handle_endtag(self, tag):
        """Handle a closing tag."""
        if not tag in self.taglevels:
            #We didn't have a strat tag for this anyway. just ignore
            return
        
        while len(self.taglevels):
            #Obtain the last tag on the list and remove it
            starttag = self.taglevels.pop()
            
            #Finish processing it
            if starttag in self.handletags:
                #If it's interesting, do something with it.
                self.finishprocessing(starttag)
            if starttag == tag:
                #Found the tag; stop processing here.
                break
    def cleanse(self):
        """Adjust data stream to convert whitespace"""
        #\xa0 is the non-breaking space (&nbsp; in HTML)
        self.data = re.sub('(\s|\xa0)+', ' ', self.data)
        sefl.data = self.data.replace("<NEWLINE>", '\n').strip()
    
    def finishprocessing(self, tag):
        """Called by handle_endtag() to handle an interesting end tag."""
        global interesting
        self.cleanse()
        if tag == 'title' and tag == self.processing:
            #Print out the page's title
            print("*** %s ***" % self.data)
        elif (tag == 'td' or tag == 'th') and tag == self.processing:
            #Got a cell in a table 获得标题
            if not self.interestingtable:
                #If we're not already in an interesting table, see if
                #this cell makes the table interesting
                for item in interesting:
                    if re.search(item, self.data, re.I): #re.I忽略大小写
                        #Yep, found an interesting table. Note that, then
                        #remove it from the interesting list, print
                        #out a heading, and stop looking at the list.
                        self.interesting = 1
                        interesting = [x for x in interesting if x != item]
                        print('\n *** %s \n' % self.data.strip())
                        break
                    else:
                        #Already in an interesting table; just add this cell to
                        #the current row
                        self.row.append(self.data)
            elif tag == 'tr' and self.interestingtable:
                #Print out an interesting row.
                self.writerow()
                self.row = []
            elif tag == 'table':
                #End of table: note that system is no longer processing
                #an interesting table.
                self.interesting = 0
                
            self.processing = None
    def writerow(self):
        """Fromats a row for on-screen display"""
        
        cells = len(self.row)
        if cells < 2:
            #If there are no cells, the row is empty;display nothing
            #If there is no cell, wunderground.com uses it as a header.
            #We don't want it, so again, display nothing.
            return
        if cells > 2:
            #If it's a table with lots of cells, give each cell
            #The same amount of space, leaving room for a space between
            #cells.
            width = (78 - cells) / cells
            mixwidth = width
        else:
            #If it's a table with two cells, make the left one narrow
            #and the right one wide.
            width = 20
            maxwidth = 58
        
        #Continue looping while at least one cell has a line of data to print
        while [x for x in self.row if x != '']:
            #Process each cell in the row.
            for i in range(len(self.row)):
                thisline = self.row[i]
                if thisline.find('\n') != -1:
                    #If it has multiple lines, we want only the frist;
                    #save it in thisline, and shove the rest back into
                    #the list for processing later.
                    (thisline, self.row[i]) = self.row[i].split('\n', 1)
                else:
                    #just one line -- we've already got it in thisline,
                    #so put the empty string in the list for later.
                    self.row[i] = ''
                thisline = thisline.strip()
                print("%-*.*s" % (width, maxwidth, thisline))
            print('\n')
    def handle_charref(self, name):
        """Process character references if possible."""
        #Validate the name.
        try:
            charnum = int(name)
        except ValueError:
            return
        if charnum < 1 and charnum > 255:
            return
        self.handle_data(chr(charnum))
        
zipcode = input("Enter ZIP code: ").strip()
url = "http://www.wunderground.com/cgi-bin/findweather/getForecast?query=" + zipcode
fd = urllib.request.urlopen(url)
parser = WeatherParser()
data = fd.read()
data = re.sub('([^ =]+)=[^ ="]+="', ' \\1="', data.decode())
data = re.sub('(?s)<!--.*?-->', "", data)
parser.feed(data)
        
        
            
                    
        