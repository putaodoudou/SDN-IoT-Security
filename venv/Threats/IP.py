import http.client
import requests
import json
from APIs.Cymon import Cymon
from Threats.Threat import Threat
from APIs.CINSS import CINSS
from APIs.Malcode import Malcode
class IP(Threat):

    def __init__(self,givenIP):
        super().__init__()
        self.IPAddress = givenIP

    #uses all APIs to search for the given IP
    #first starts with cymon
    def checkIP(self):
        if(self.__checkWithCymon()):
            return True
        if (self.__checkWithCINSS()):
            return True
        if(self.__checkWithMalcode()):
            return True
        return False

    #this function connects to cymon API and searches for any records about the IP address
    def __checkWithCymon(self):
        cymon = Cymon("pbolkas", "Hx7_=9%JSj*ru6HNFQ")
        cymon.login()

        url = "/ioc/search/ip/"+ self.IPAddress+"?size=0"
        results = cymon.get(url)
        total = results.json().get('total')

        if total > 0: #that means that has found some malicious records
            return True
        return False

    #this function searches in a file that malicious IPs are stored from CINSS source
    def __checkWithCINSS(self):
        cinss = CINSS()
        return cinss.compareIP(self.IPAddress)

    def __checkWithMalcode(self):
        #create object
        malcode = Malcode()
        #fill the lists
        malcode.makeXML()
        #check the ip
        return malcode.checkIP(self.IPAddress)

    def __checkWithNormShield(self):
        None

'''
#test methods
ip1 = IP('54.236.22.32')
print('This ip is considered as malicious '+str(ip1.checkIP()))
'''

