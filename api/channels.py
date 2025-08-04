from scraper import fetch_channels

def handler(request, response):
    channels = fetch_channels()
    return response.json(channels)
