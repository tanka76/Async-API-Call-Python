import requests
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key=os.getenv('H55WKU0AIZF931N2')
symbols=['IBM','GOOG','TSLA','AAPL']

res=[]
start=time.time()

for symbol in symbols:
    print("Working on Symbol",symbol)
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&interval=5min&apikey={api_key}'
    resp=requests.get(url=url)
    data=resp.json()
    res.append(data)

end=time.time()
total_time=end-start
print("Total Time Taken",total_time)
# print("Okay! After API Call",res)