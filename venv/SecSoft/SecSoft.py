import http.client
import requests
import json
from APIs.Cymon import Cymon
from Threats.Email import Email
from Threats.IP import IP
from Utilities.Dispatcher import Dispatcher
from Threats.URL import URL

#This will be the file that will be examined
LogFile = None

#below some threat examples

threatIP = IP( "250.240.230.220")
threatURL = URL("google.gr")
threatEmail = Email("p.bolkas@gmail.com")
threatFile = ""

class SecSoft:

    def __init__(self):
        self.dispatcher = Dispatcher()

    #this function reads the log file and examines whether an sdn station
    #is infected by a Threat or not
    def checkThreat(self):

        self.dispatcher.enqueue(threatURL)
        self.dispatcher.enqueue(threatIP)
        self.dispatcher.enqueue(threatEmail)



        return # returns a report in a form of an array that explains which station is infected by which threat

    #the below method sniffs the network and finds ip addresses, email addresses and urls
    #under construction
    def sniffNetwork(self):

        #sniff the network
        #find candidate threats
        #add these threats to Dispatcher

        return

    #the below method reads the sdn log and searches for IP addresses, URLs, Email addresses and Files
    #under construction
    def readLog(self):

        #read sdn log
        #find candidate threats
        #add these threats to Dispatcher

        return


ss = SecSoft()
ss.checkThreat()



