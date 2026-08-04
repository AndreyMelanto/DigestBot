from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command('news'))
async def news(message: types.Message):
    await message.answer('news')


@router.message(Command('fact'))
async def fact(message: types.Message):
    await message.answer('fact')


@router.message(Command('currency'))
async def currency(message: types.Message):
    await message.answer('currency')


@router.message(Command('digest'))
async def digest(message: types.Message):
    await message.answer('digest')
