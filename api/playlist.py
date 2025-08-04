from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/api/playlist", response_class=PlainTextResponse)
def playlist():
    res = requests.get('https://okteve.com/channels')
    soup = BeautifulSoup(res.text, 'html.parser')
    m3u = "#EXTM3U\n"
    for item in soup.select('.channel-item'):
        name = item.select_one('.channel-name').text.strip()
        url = item.select_one('a')['href']
        m3u += f"#EXTINF:-1,{name}\n{url}\n"
    return m3u
