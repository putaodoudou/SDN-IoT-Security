#this class is used as a new Thread for each threat that exists in the threatQueue
#this class contains all the appropriate methods to examine a threat
from threading import Thread
from Threats.Email import Email
from Threats.File import File
from Threats.URL import URL
from Threats.IP import IP
class Examine (Thread):

    def __init__(self,theThreat):
        super().__init__(None,None,name
        ="Examine "+str(theThreat), args={},kwargs=None, daemon=None)
        self.threat=theThreat

    #overrided method
    #this method starts the threat investigation
    #and returns the value that is
    def run(self):
        print("Thread started "+self.name)
        return self.investigation()


    #this method investigates the threat with the classes
    #declared in Threats.* package
    def investigation(self):
        if (type(self.threat) is Email):
            #check if this email address is malicious

            #first downcast to the Emaik class
            self.threat.__class__ = Email
            #then create new instance of the under investigation object
            email = self.threat

            return email.checkEmail()

        elif (type(self.threat) is File):
            #check if this File (name, hash, whole file) is malicious
            #first downcast the threat
            self.threat.__class__ = File
            file = self.threat
            #now should examin it with the functions of the file class
            return file.checkHash()

        elif (type(self.threat) is IP):
            #check if this IP is malicious
            #first downcast the threat to ip
            self.threat.__class__ = IP
            ipAddress = self.threat

            return ipAddress.checkIP()

        elif (type(self.threat) is URL):
            #check if this URL address is malicious
            #first downcast the threat to URL

            self.threat.__class__ = URL
            url = self.threat

            return url.checkURL
        return False
