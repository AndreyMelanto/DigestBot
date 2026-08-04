import aiohttp
from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command('start'))
async def start(message: types.Message, session: aiohttp.client.ClientSession):
    await message.answer('start')


@router.message(Command('help'))
async def help_(message: types.Message, session: aiohttp.client.ClientSession):
    await message.answer('help')
