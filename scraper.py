import requests
from bs4 import BeautifulSoup

def fetch_channels():
    url = 'https://okteve.com/channels'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    channels = []
    # Adjust HTML selectors based on actual structure
    for item in soup.select('.channel-item'):
        name = item.select_one('.channel-name').text.strip()
        stream_url = item.select_one('a')['href']
        channels.append({
            'name': name,
            'url': stream_url
        })

    return channels
