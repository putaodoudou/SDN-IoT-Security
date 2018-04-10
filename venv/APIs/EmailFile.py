import requests
import os
class EmailFile:

    def __init__(self):
        None

    def downloadFile(self):

        #if this file already exists don't download it again
        #later should be added a date check to update this file
        if(os.path.isfile('./MaliciousEmailFile.txt')):
            return

        #connect to url and request the malware-email-address file
        response = requests.get('https://raw.githubusercontent.com/WSTNPHX/scripts-n-tools/master/malware-email-addresses.txt', stream= True)
        #save the response
        data = response.text


        # Write data to file
        filename = "MaliciousEmailFile.txt"
        file_ = open(filename, 'w')
        file_.write(str(data))
        file_.close()

    def checkTheEmail(self,Email):

        #this method opens the file where mailicous email addresses are
        # stored and compares each of them with the given email
        with open('./MaliciousEmailFile.txt','r') as fp:
            line = fp.readline()
            while line:
                if(line.strip() == str(Email)):
                    print(line.strip())
                    fp.close()
                    return True
                line = fp.readline()

        fp.close()


        return False
