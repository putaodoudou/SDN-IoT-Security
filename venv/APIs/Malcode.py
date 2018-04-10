import urllib3
from xml.etree import  ElementTree as etree
from Threats.Threat import Threat
class Malcode:

    def __init__(self):
        #below private method that updates that data obtained from the rss feed
        self.data = self.__getRSSData()

        #here is defined the three lists that this API offers
        #from this list comparances will be executed to check either a URL, an IP or a Hash
        self.URLList = []
        self.IPList = []
        self.HashList =[]



    #updates RSS data
    def __getRSSData(self):
        http = urllib3.PoolManager()

        url = 'http://malc0de.com/rss/'

        response = http.request('GET', url)

        return response.data

    #manipulates rss and creates xml data and then calls createThreatObjects
    def makeXML(self):
        feedRoot = etree.fromstring(self.data)
        item = feedRoot.findall('channel/item')
        #print (item)

        feed =[]

        for entry in item:
            desc = entry.findtext('description')
            feed.append([desc])

        self.__createThreatObjects(feed)

    #this method takes each xml element that contains useful data such as url, ips and hashes
    #and calls manipulateString that will add in lists the malicious data like URL, ip or hash
    def __createThreatObjects(self,feed):
        for row in feed:
            threat = self.__manipulateString(str(row))

    #this method takes a row from the rss feed and fills the lists from which the log files will be checked
    #that contains URL, IP address and HASH
    def __manipulateString(self,row):
        URL = ''
        IPAddress = ''
        Email =''
        HASH = ''
        content = ''
        flag = False
        count =0

        #replaces some special characters with ',' and selects between some commas to find URL, IPAddress and Hash values
        row = row.replace( ':',',')
        row = row.replace('\'',',')
        URL = row.split(',')[2].strip()
        IPAddress = row.split(',')[4].strip()
        HASH = row.split(',')[10].strip()

        self.URLList.append(URL)
        self.IPList.append(IPAddress)
        self.HashList.append(HASH)

    #this searches in ip list to find if parameter IPAddress is included in malicious IP List
    def checkIP(self,IPAddress):
        for current in self.URLList:
            if(current == IPAddress):
                return True
        return False

    #this method searches inside URL list and compares the given URL to find if it is malicious or not
    def checkURL(self,URL):
        for current in self.URLList:
            if current == URL:
                return True
        return False

    #this method searches to Hash list to finde if the given hash is included in malicious hash list or not
    def checkHash(self,Hash):
        for current in self.HashList:
            if (current == Hash):
                return True
        return False


#test methods
#create object
m = Malcode()


#store lists properly
m.makeXML()
#call each category to test
'''
print('this ip is considered as malicious '+str(m.checkIP('173.254.56.13')))
print('this md5 hash is considered as malicious '+str(m.checkHash('487ffc5882412dada9102ec6ea9d5d29')))
print('this url is considered as malicious '+str(m.checkURL('http://www.google.gr')))
'''
