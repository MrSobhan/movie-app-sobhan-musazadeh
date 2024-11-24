# import required modules
import os
from time import sleep
import random 
# list of VPN server codes 
codeList = ["TR", "US-C", "US", "US-W", "CA", "CA-W", "FR", "DE", "NL", "NO", "RO", "CH", "GB", "HK"]
try: 
# connect to VPN 
  os.system("windscribe connect") 
  while True: 
    # assigning a random VPN server code
    choiceCode = random.choice(codeList) 
# changing IP after a particular time period
    sleep(random.randrange(120, 300))
# connecting to a different VPN server print("!!! Changing the IP Address........") 
    os.system("windscribe connect " + choiceCode)
    except:
# disconnect VPN 
      os.system("windscribe disconnect") print("sorry, some error has occurred
