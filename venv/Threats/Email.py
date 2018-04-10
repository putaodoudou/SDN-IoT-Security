import codecs
import http.client
import requests
import json
from APIs.EmailFile import EmailFile
from Threats.Threat import Threat
class Email(Threat):


    def __init__(self,Email):
        super().__init__()
        self.Email= Email
        #self.blacklist =  codecs.open('https://raw.githubusercontent.com/WSTNPHX/scripts-n-tools/master/malware-email-addresses.txt','r')


    #Engine is about the API of the malicious Email repository
    #will be used to check this email
    #this method calls other methods that connect to APIs or read files to identify if the given Email is a threat
    def checkEmail(self):
        if(self.__checkFromFile()):
            self.result = True
            return True
        #now should check the other API
        self.__checkFromAnotherSource()
        self.result = False

        return False

    #This method checks the email from a file, it calls a method inside APIs/EmailFile.py file
    def __checkFromFile(self):
        emailFile = EmailFile()
        emailFile.downloadFile()
        if(emailFile.checkTheEmail(self.Email)):
            return True
        return False

    def __checkFromAnotherSource(self):
        None
        #this method searches to a different source for malicious email

'''
#test methods
em=Email('2016banklogins@gmail.com')
print('this email is considered malicious: '+str(em.checkEmail()))
'''
