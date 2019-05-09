import requests
import os

dweetIO = "https://dweet.io/dweet/for/"
myName = "Objeto"
myKey = "temp"

tempC = []

for i in range(0,26):
    tempC.append(0)
    
while True:

    ostemp = os.popen('vcgencmd measure_temp').readline()
    temp = (ostemp.replace("temp=", "").replace("'C\n", ""))
 #   print(temp)
    tempC.append(temp)
    tempC.pop(0)

    #Send to Cloud, dweet.io
    rqsString = dweetIO+myName+'?'+myKey+'='+str(temp)
#    rqsString = dweetIO+myName+'?'+myKey+'='+str(temp)+'&'+myLink
#    print(rqsString)
    rqs = requests.get(rqsString)
#    print (rqs.status_code)
#    print (rqs.headers)
#    print (rqs.content)
    
#    plt.pause(.5)
