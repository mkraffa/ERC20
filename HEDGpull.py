
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

#range to max value, or edit for specific addresses
#HEDG
for i in range(20):
    try:
        Contract = "0xf1290473e210b2108a85237fbcd7b6eb42cc654f"
        Address = df['pub'].iloc[i]
        url = "https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress="+Contract+"&address="+Address+"&tag=latest&apikey="+API
        response = requests.get(url)
        data = response.text
        parsed = json.loads(data)
        supply = parsed['result']
        supply = int(supply)/1000000000000000000
        df.at[i,'HEDG'] = supply
        print("address at index "+str(i)+" had "+str(supply)+" HEDG")
    except: print('parsing error')    
    
#save to CSV    
df.to_csv('tracked_addresses', index=False)
