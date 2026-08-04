import asyncio

import aiohttp
from aiogram import Router, types
from aiogram.filters import Command

import services
from formatting import format_news, format_currency, format_digest
from utils import safe_fetch

router = Router()


@router.message(Command('news'))
async def news(message: types.Message, session: aiohttp.client.ClientSession):
    data = await safe_fetch(services.get_news(session))
    text = format_news(data)
    await message.answer(**text.as_kwargs())


@router.message(Command('fact'))
async def fact(message: types.Message, session: aiohttp.client.ClientSession):
    await message.answer(await services.get_fact(session))


@router.message(Command('currency'))
async def currency(message: types.Message, session: aiohttp.client.ClientSession):
    data = await services.get_currency(session)
    await message.answer(format_currency(data))


@router.message(Command('digest'))
async def digest(message: types.Message, session: aiohttp.client.ClientSession):
    news_task = asyncio.create_task(services.get_news(session))
    fact_task = asyncio.create_task(services.get_fact(session))
    currency_task = asyncio.create_task(services.get_currency(session))

    data = await asyncio.gather(news_task, fact_task, currency_task)

    await message.answer(
        format_digest(data),
        parse_mode='html'
    )
