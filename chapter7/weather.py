#Weather Parser -chapter 7- weather.py

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