import asyncio
import aiohttp
import feedparser

from endpoints import HABR_URL, FACTS_URL, CENTRAL_BANK_URL
from utils import translate, safe_fetch


async def get_news(session: aiohttp.ClientSession):
    async with session.get(HABR_URL) as response:
        response.raise_for_status()
        xml = await response.text()
    parsed = await asyncio.to_thread(feedparser.parse, xml)
    return [{"title": entry.title, "link": entry.link} for entry in parsed.entries[:5]]


async def get_fact(session: aiohttp.ClientSession):
    async with session.get(FACTS_URL) as response:
        response.raise_for_status()
        eng_text = (await response.json())['text']

    rus_text = await translate(eng_text, session)
    return rus_text['translations'][0]['text']


async def get_currency(session: aiohttp.ClientSession):
    async with session.get(CENTRAL_BANK_URL) as response:
        response.raise_for_status()
        return [(await response.json(content_type=None))['Valute'][key] for key in ['USD', 'EUR']]
