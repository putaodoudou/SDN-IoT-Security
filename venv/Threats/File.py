from APIs.Malcode import Malcode
from Threats.Threat import Threat
from subprocess import check_output
import  subprocess
import  re

class File(Threat):

    #here are defined fileName (optional) and fileHash
    def __init__(self,name,hash,file):
        super().__init__()
        self.name=name
        self.hash=hash
        self.file = file #this is the entire file with a "File" form

    #checkHash connects to APIs and searches for malicious correlations between sources and the given hash
    def checkHash(self):
        if(self.__checkHashWithMalcode()):
            return True
        return False
    #this method connects to Malcode API to search from it if the given hash is malicious
    def __checkHashWithMalcode(self):
        #create object
        malcode = Malcode()
        #fill the lists
        malcode.makeXML()
        #check the fileHash
        return malcode.checkHash(self.hash)

    #this function is used to compare two files using fuzzy hashing and find their similarities
    #the first file should be the known threat and the second file should be the under investigation file
    #this function creates a results file where the similarity percentage will be found
    def fuzzyHashCheck(self,knownThreat):
        command = "ssdeep -h"
        command = "dir"

        print((check_output(command,shell=True)))
        command = "cd .."

        print((check_output(command,shell=True)))
        command = "dir"

        print((check_output(command,shell=True)))
        command = "cd ../sdeepfiles/known_threats" #this leads to the path of the known threat




        #print((check_output(command,shell=True)))

        return

'''
f = File("noName","487ffc5882412dada9102ec6ea9d5d29","f")
#print('This file is considered as malicious '+str(f.checkHash()))
'''

