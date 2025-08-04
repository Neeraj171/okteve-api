from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/api/channels")
def channels():
    res = requests.get('https://okteve.com/channels')
    soup = BeautifulSoup(res.text, 'html.parser')
    channels = []
    for item in soup.select('.channel-item'):
        name = item.select_one('.channel-name').text.strip()
        url = item.select_one('a')['href']
        channels.append({'name': name, 'url': url})
    return JSONResponse(content=channels)
