#Date Parsing -Chapter 9- date_parse.py
#This program requires Python 2.2.2 or above

import sys, email, time
from email import utils

def getdate(msg):
    """Return the date/time from msg in seconds-since-epoch, if possible.
    otherwise, returns None."""
    
    if not 'date' in msg: #先看看有木有dateheader
        #No Date header present.
        return None
    datehdr = msg['date'].strip()
    try:
        return utils.mktime_tz(utils.parsedate_tz(datehdr))
    except:
        #Some sort of error occured, likely beacuse of an invaild date.
        return None

fd = open('message.txt', mode='r')
msg = email.message_from_file(fd)
fd.close()

dateval = getdate(msg)
if dateval is None:
    print('No Vaild date was found.')
else:
    print("Message was sent on", time.strftime('%A, %B, %d %Y at %I:%M %p', time.localtime(dateval)))