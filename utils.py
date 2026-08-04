import asyncio
import aiohttp

from config import DEEPL_API_KEY
from endpoints import DEEPL_API_URL


class FetchError:
    def __init__(self, message):
        self.message = message


async def safe_fetch(coro, timeout: float = 6.7):
    try:
        return await asyncio.wait_for(coro, timeout=timeout)
    except asyncio.TimeoutError:
        return FetchError(f"Timed out while fetching {coro.__name__}")
    except aiohttp.ClientError as e:
        return FetchError(str(e))


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
