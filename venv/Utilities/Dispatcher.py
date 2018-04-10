#here will exist a queue where all of the Threats will be stored
# and for each threat that we pull out the queue there will be
# created a new Tread to execute
# a search from the APIs
import  queue
from Threats.Email import  Email
from Threats.File import File
from Threats.IP import IP
from Threats.Threat import Threat
from Threats.URL import URL
import _thread
import time
from Utilities.Examine import Examine
class Dispatcher:

    def __init__(self):
        self.threatQueue = queue.Queue() # the queue that every Threat will be stored

    #this method is used to enqueue a new threat
    def enqueue(self,threat):
        #puts threat to the queue
        self.threatQueue.put_nowait(threat)

        return

    #this method is used to dequeue a Threat and examine it
    def dequeue(self):
        currentTail = self.threatQueue.get_nowait()
        return currentTail

    #this method examines the tail of the queue ( the item that is dequeued)
    #this method returns True if the under examination threat is truly a threat or
    # False if the under examination threat is not actually a threat
    def examine(self):
        threatToExamine = self.dequeue()
        #create Examine Thread
        e = Examine(threatToExamine)

        e.start()
        return

    #the method below is executed in a Thread and
    # detects any threats inside the queue
    # as soon as it detects a new threat it creates a new Thread
    #to examine the current threat
    def threatThreadIgnition(self):
        while True:
            if self.threatQueue.qsize() >0 :
                self.examine()


        return

    def startThreatSearch(self):
        try:
            #define the Thread and start it
            #this line declares a new thread and starts it
            #this thread will be wxecuted for ever
            #because of the while (true) loop that exists in the threatThreadIgnition function
            _thread.start_new_thread(self.threatThreadIgnition,())

        except Exception as e:
            print(str(e))
        while 1:
            pass



d = Dispatcher()

emailThreat = Email("aalvriyanto@gmail.com")
IPThreat = IP("175.195.178.81")
URLThreat = URL("www.google.gr")
emailThreat2 = Email("aalvriyanto@gmail.com")
emailThreat3 = Email("aalvriyanto.com")
emailThreat4 = Email("aalvrimail.com")
fileThreat= File("filename","abcd hash",None)

d.enqueue(emailThreat)
d.enqueue(IPThreat)
d.enqueue(emailThreat2)
d.enqueue(emailThreat3)
d.enqueue(emailThreat4)
d.enqueue(URLThreat)
d.enqueue(fileThreat)

d.startThreatSearch()
print("the first email is considered as malicious "+str(emailThreat.result))

