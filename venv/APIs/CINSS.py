import requests
import urllib3
import os
class CINSS:

    def __init__(self):
        None

    def updateRepository(self):
        #if this file already exists don't download it again
        if(os.path.isfile('./ipRepositoryFromCINSS.txt')):
            return

        #connect to url and request the ci-badguys.txt file
        response = requests.get('http://cinsscore.com/list/ci-badguys.txt', stream= True)
        #save the response
        data = response.text


        # Write data to file
        filename = "ipRepositoryFromCINSS.txt"
        file_ = open(filename, 'w')
        file_.write(str(data))
        file_.close()


    def compareIP(self,address):
        #opens a file with malicious ip addresses and reads it line by line to find if the given ip  is malicious or not
        #this method returns True if it is considered as a threat or False if it is not included in threat ip list that exists in the file
        self.updateRepository()
        with open('./ipRepositoryFromCINSS.txt','r') as fp:
            line = fp.readline()
            while line:
                if(line.strip() == str(address)):
                    fp.close()
                    return True
                line = fp.readline()

        fp.close()
        return False
