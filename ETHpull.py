#API Method
import pandas as pd
import numpy as np
import webbrowser
import requests, bs4
import json
from urllib.request import Request, urlopen

#see CSV template and fill accordingly
df = pd.read_csv('tracked_addresses.csv')

#get your API key here: https://etherscan.io/apis
API = ""

#ETH doesn't require Contract specification
#range to max value, or edit for specific addresses
startTime = datetime.now()
for i in range(20):
    try:
        Address = df['pub'].iloc[i]
        url = "https://api.etherscan.io/api?module=account&action=balance&address="+Address+"&tag=latest&apikey="+API
        response = requests.get(url)
        data = response.text
        parsed = json.loads(data)
        supply = parsed['result']
        supply = int(supply)/1000000000000000000
        df.at[i,'ETH'] = supply
        print("address at index "+str(i)+" had "+str(supply)+" ETH")
    except: print('parsing error')
    
#sace to CSV    
df.to_csv('tracked_addresses', index=False)
#print operation duration
print(datetime.now() - startTime)
