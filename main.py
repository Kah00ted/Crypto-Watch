import requests
import json
import time
from pcNotif import *

# ---user config---
#coin
symbol = "SAFEMOON"

#lunarcrush api
apiKey = "xwe7noxgswhw5cbqhjnnrm"

#pricing to notify
notifLow = 0.000004
notifHigh = 0.000008

url = "https://api.lunarcrush.com/v2/?key="+apiKey+"&symbol="+symbol+"&data=assets"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

coinJson = json.loads(response.text)
coinPrice = coinJson["data"][0]["price"]
coinPriceNumber = '{0:.10f}'.format(coinJson["data"][0]["price"])

print(coinPriceNumber)

def checkCrypto():
    if (coinPrice <= notifLow):
        print("buy")
        displayNotif("Crypto Watch - BUY", symbol+": "+str(coinPriceNumber), True)
    elif (coinPrice >= notifHigh):
        print("sell")
        displayNotif("Crypto Watch - SELL", symbol+": "+str(coinPriceNumber), True)
    else:
        print("hold")

while (5>1):
    checkCrypto()
    time.sleep(3)