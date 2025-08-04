from scraper import fetch_channels

def handler(request, response):
    channels = fetch_channels()
    m3u = "#EXTM3U\n"
    for ch in channels:
        m3u += f"#EXTINF:-1,{ch['name']}\n{ch['url']}\n"
    return response.send(m3u, content_type='audio/x-mpegurl')
