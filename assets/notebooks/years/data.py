import asyncio  
import aiohttp
import pandas as pd
import requests
import concurrent.futures
import json
import time
import urllib.parse

lyrics = dict()
async def get_lyrics(lyrics_url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                executor, 
                requests.get, 
                url
            )
            for url in lyrics_url
        ]
        lyrics_list = []
        for response in await asyncio.gather(*futures):
            if response.status_code == 200:
                lyrics_list.append(json.loads(response.text)['lyric'].replace('\n', ' '))
            else:
                lyrics_list.append("")
    return lyrics_list

lyrics_url = []
print("Loading Data...")
raw = pd.read_csv("songlist.txt", header=None, names=['songs'])
print("Data loaded!")
lyrics_url = raw.songs.apply(lambda x : 'http://lyric-api.herokuapp.com/api/find/years%20&%20years/' + urllib.parse.quote(x.lower())).values
print("List ready!")
start_time = time.time()
loop = asyncio.get_event_loop()
lyrics = loop.run_until_complete(get_lyrics(lyrics_url))
loop.close()
print("--- %s seconds ---" % (time.time() - start_time))
lyrics = pd.Series(lyrics)
lyrics.name = "Lyrics"
raw = pd.concat([raw, lyrics], axis=1)
raw.to_csv("lyrics.csv")