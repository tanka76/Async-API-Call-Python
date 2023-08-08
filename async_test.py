import requests
import asyncio
import aiohttp
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key=os.getenv('H55WKU0AIZF931N2')
symbols=['IBM','GOOG','TSLA','AAPL']

res=[]

async def get_stock():
    start=time.time()
    async with aiohttp.ClientSession() as session:
        for symbol in symbols:
            print("Working on Symbol",symbol)
            url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&interval=5min&apikey={api_key}'

            resp=await session.get(url=url,ssl=False)
            data=await resp.json()
            res.append(data)
    
    end=time.time()
    total_time=end-start
    return total_time

total_time=asyncio.run(get_stock())
print("Total Time Taken",total_time)
# print("Okay! After API Call",res)