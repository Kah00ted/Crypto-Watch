import requests
import json
import time

# ---user config---
#coin
symbol = "safemoon"

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

print('{0:.10f}'.format(coinJson["data"][0]["price"]))

def checkCrypto():
    if (coinPrice <= notifLow):
        print("buy")
    elif (coinPrice >= notifHigh):
        print("sell")
    else:
        print("hold")

while (5>1):
    checkCrypto()
    time.sleep(3)