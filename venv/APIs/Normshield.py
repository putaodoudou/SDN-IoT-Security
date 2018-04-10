import requests

# this class is under construction is not yet finished
#not recommended to use !!!!!!!!!!!!!
class Normshield:

    def __init__(self):
        #The main URL of the API
        self.endpoint = 'https://services.normshield.com/api/v1/'

        #the categories for each API usage
        self.DomainSearch = 'phishing/domain'
        self.IPBlacklist = 'blacklist/searchip'
        self.BreachEmail = 'breach/email'
        self.BreachDomain = 'breach/domain'
        self.h = {
           'Content-Type': 'application/json'
        }


    #this function searches for dns lookup records
    def postDomainSearch(self,domain):
        params = {'domain': domain}

        r = requests.post(self.endpoint + self.DomainSearch, json=params, headers=self.h)
        r.raise_for_status()
        return r
    #this method searches for ip threat records that are related to the given ip
    def postIPBlacklist(self, ip):
        params = { 'ip' : ip}
        r = requests.post(self.endpoint + self.IPBlacklist, json=params, headers=self.h)
        r.raise_for_status()
        return r
    #this method searches for email threat records that are related to the given email address
    def postEmailSearch(self,email):
        params = {'email' : email}
        r = requests.post(self.endpoint + self.BreachEmail, json=params, headers=self.h)
        r.raise_for_status()
        return r
    #this method searches for domain threat records that are related to the given domain name
    def postBreachDomain(self,domain):
        params = {'domain' : domain}
        r= requests.post(self.endpoint + self.BreachDomain, json=params, headers=self.h)
        r.raise_for_status()
        return r



n = Normshield()

url="b.reich.io"
#print(n.postDomainSearch(url).status_code)
print(n.postDomainSearch(url).text)

ip = "54.236.22.32"

ip = "5.228.91.219"

print(n.postIPBlacklist(ip).text)



email = "2016banklogins@gmail.com"
email = "carlosromero19871@gmail.com"

dom = 'google.gr'


#print(n.postBreachDomain(dom).text)
#print(n.postEmailSearch(email).text)



