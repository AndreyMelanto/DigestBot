import aiohttp
import feedparser

from urls import HABR_URL


async def get_news(session: aiohttp.ClientSession):
    async with session.get(HABR_URL) as response:
        xml = await response.text()
    parsed = feedparser.parse(xml)
    return [{"title": entry.title, "link": entry.link} for entry in parsed.entries[:5]]
