import aiohttp
import feedparser

from urls import HABR_URL, FACTS_URL
from utils import translate


async def get_news(session: aiohttp.ClientSession):
    async with session.get(HABR_URL) as response:
        xml = await response.text()
    parsed = feedparser.parse(xml)
    return [{"title": entry.title, "link": entry.link} for entry in parsed.entries[:5]]


async def get_fact(session: aiohttp.ClientSession):
    async with session.get(FACTS_URL) as response:
        eng_text = (await response.json())['text']

    rus_text = await translate(eng_text, session)
    return rus_text['translations'][0]['text']
