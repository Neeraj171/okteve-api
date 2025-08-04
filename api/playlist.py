const chromium = require('@sparticuz/chromium');
const puppeteer = require('puppeteer-core');

module.exports = async (req, res) => {
  const browser = await puppeteer.launch({
    args: chromium.args,
    defaultViewport: chromium.defaultViewport,
    executablePath: await chromium.executablePath(),
    headless: chromium.headless,
  });
  const page = await browser.newPage();
  await page.goto('https://okteve.com/channels', { waitUntil: 'networkidle2' });
  const channels = await page.evaluate(() => {
    const items = document.querySelectorAll('.channel-item');
    return Array.from(items).map(el => ({
      name: el.querySelector('.channel-name')?.innerText.trim(),
      url: el.querySelector('a')?.href
    }));
  });
  await browser.close();

  let m3u = "#EXTM3U\n";
  channels.forEach(ch => {
    m3u += `#EXTINF:-1,${ch.name}\n${ch.url}\n`;
  });
  res.setHeader('Content-Type', 'audio/x-mpegurl');
  res.send(m3u);
};
