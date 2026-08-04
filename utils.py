import asyncio
import aiohttp

from config import DEEPL_API_KEY
from urls import DEEPL_API_URL


async def safe_fetch(coro, timeout: float = 6.7):
    try:
        return await asyncio.wait_for(coro, timeout=timeout)
    except asyncio.TimeoutError:
        return {'error': 'timed out'}
    except aiohttp.ClientError as e:
        return {'error': str(e)}


async def translate(text: str, session: aiohttp.ClientSession):
    headers = {
        "Authorization": "DeepL-Auth-Key " + DEEPL_API_KEY,
    }
    data = {
        "text": [text],
        "source_lang": "EN",
        "target_lang": "RU"
    }
    async with session.post(url=DEEPL_API_URL, headers=headers, data=data) as response:
        response.raise_for_status()
        return await response.json()
