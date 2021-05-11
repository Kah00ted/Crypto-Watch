import requests
import json

# ---user config---
#coin
symbol = "safemoon"

#lunarcrush api
apiKey = "xwe7noxgswhw5cbqhjnnrm"

url = "https://api.lunarcrush.com/v2/?key="+apiKey+"&symbol="+symbol+"&data=assets"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

coinJson = json.loads(response.text)

print('{0:.10f}'.format(coinJson["data"][0]["price"]))