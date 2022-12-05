import logging

from fetch_facts import *
from TOKEN_API import token_api

import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor


logging.basicConfig(level=logging.INFO)

bot = Bot(token=token_api)
storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)

class Form(StatesGroup):
    name = State()
    is_cat = State()
    is_picture = State()

@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    logging.info('Canceling state %r', current_state)
    await state.finish()
    await message.reply('Cancelled', reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await Form.name.set()

    await message.reply('Hi what is your name?')

@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add('Cat', 'Dog', 'None of that')
    await Form.next()
    print('1'*100)
    await message.reply('Are you cat or god lover?', reply_markup=markup)

@dp.message_handler(lambda message: message.text not in ['Cat', 'Dog', 'None of that'], state=Form.is_cat)
async def process_is_cat_invalid(message: types.Message):
    return await message.reply('Please choose from your keyboard')


@dp.message_handler(state=Form.is_cat)
async def process_is_cat(message: types.Message, state: FSMContext):
    if message.text == 'None of that':
        await state.finish()
        markup = types.ReplyKeyboardRemove()
        return await bot.send_message(
            message.chat.id,
            "Lol what are you doing here? Change your mind and try again later")
    msg = message.text
    async with state.proxy() as data:
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Hi, '),
                md.bold(data['name']),
                md.text(' your fact: '),
                md.text(get_cat_fact() if message.text == 'Cat' else get_dog_fact())
            )
    )        
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
