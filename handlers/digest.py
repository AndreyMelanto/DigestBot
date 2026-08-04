import aiohttp
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.formatting import Text, TextLink, as_line

import services
from utils import safe_fetch

router = Router()


@router.message(Command('news'))
async def news(message: types.Message, session: aiohttp.client.ClientSession):
    data = await safe_fetch(services.get_news(session))
    text = Text(
        'Последние новости:\n\n',
        *[as_line(as_line(TextLink(el['title'], url=el['link']))) for el in data],
    )
    await message.answer(**text.as_kwargs())


@router.message(Command('fact'))
async def fact(message: types.Message, session: aiohttp.client.ClientSession):
    await message.answer(await services.get_fact(session))


@router.message(Command('currency'))
async def currency(message: types.Message, session: aiohttp.client.ClientSession):
    await message.answer('currency')


@router.message(Command('digest'))
async def digest(message: types.Message, session: aiohttp.client.ClientSession):
    await message.answer('digest')
