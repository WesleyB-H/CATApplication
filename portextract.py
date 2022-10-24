#Written by Wesley Berman-Hershko on 10/22/2022
#Purpose of this script is to cleanly parse log data from various log sources.
#Note: As new log types would be added, this script would keep things easy to understand and additional log types could be added in easily.
import re

class logInjest:

    #Constructor Init...
    def __init__(self):
        self.allLogs=[]

    #Reads in lines from general log file. (No blank lines allowed in file for this use case please)
    def importLogs(self):
        with open('logs.txt') as fIn:
            text= fIn.read()
            tempArray=text.split("\n")
            self.allLogs = tempArray

    #Uses anchors to parse logs regardless of source type. Could parse all fields from all log types from one file using this method.
    def parseLogs(self):
        for log in self.allLogs:
            try:
                dateAnchor = re.search("\>.{1,}\s(okc|OKC)", log).group(0)
                date = re.search("([A-za-z]{3}|\d{4}).{1,} ", dateAnchor).group(0)[:-1]
            except:
                date=""
            try:
                hostName = re.search("(OKC|okc)[A-Za-z0-9\.\-]{1,}", log).group(0)
            except:
                hostName=""
                
            try:
                userNameAnchor = re.search("(user|Name).{1,}(from|Acc)", log).group(0)
                userName = userNameAnchor.split(" ")[1]
            except:
                userName=""

            try:
                portAnchor = re.search("(port|Port).{1,2}\d{1,}", log).group(0)
                port = re.search("\d{1,5}", portAnchor).group(0)
            except:
                port=""
                
            try:
                srcIPAnchor = re.search("(from|src|Client).{1,}(\d{1,3}\.){3}\d{1,3}", log).group(0)
                srcIP = re.search("(\d{1,3}\.){3}\d{1,3}", srcIPAnchor).group(0)
            except:
                srcIP=""
                
            try:
                dstIPAnchor = re.search("dst.{1,}(\d{1,3}\.){3}\d{1,3}.{1,}log", log).group(0)
                dstIP = re.search("(\d{1,3}\.){3}\d{1,3}", dstIPAnchor).group(0)
            except:
                dstIP=""
                
            print("Raw Log: " + log + "\n")
            print("Parsed Log:\n" + "Date: " + date + "\nHostname: " + hostName + "\nUsername: " + userName + "\nPort: " + port + "\nSource IP: " + srcIP + "\nDest IP: " + dstIP + "\n")

#Initial Configuration....
testObject=logInjest()
testObject.importLogs()
testObject.parseLogs()
