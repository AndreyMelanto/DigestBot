import aiohttp
from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Это жоски бот\n\n/help - список команд')


@router.message(Command('help'))
async def help_(message: types.Message):
    await message.answer('/news - последние пять новостей с Хабра\n/fact - рандомный факт\n/currency - курсы доллара и евро\n/digest - ПОЛНЫЙ ЖОСКИЙ ДАЙДЖЕСТ')
