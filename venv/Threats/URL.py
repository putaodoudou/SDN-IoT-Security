from APIs.Malcode import Malcode
from Threats.Threat import Threat
class URL(Threat):

    def __init__(self,URL):
        super().__init__()
        self.url = URL


    def checkURL(self): #connects to domain source API and searches for malicious Domain
        if(self.__checkWithMalcode()):
            return True
        return False

    def __checkWithMalcode(self):
        #create object
        malcode = Malcode()
        #fill the lists
        malcode.makeXML()
        #check the url
        return malcode.checkURL(self.url)

'''
url = URL('lashawnbarber.com/images/files/mii.exe')
print('This url is considered as malicious '+str(url.checkURL()))
'''

