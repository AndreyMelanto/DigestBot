import asyncio

import aiohttp
from aiogram import Bot, Dispatcher

from config import TOKEN
from handlers.common import router as common_router
from handlers.digest import router as digest_router


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(common_router)
    dp.include_router(digest_router)
    async with aiohttp.ClientSession() as session:
        dp['session'] = session
        await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
