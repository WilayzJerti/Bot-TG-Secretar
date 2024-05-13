import asyncio
import logging

from aiogram import F, Bot, Dispatcher, types
from aiogram.filters.command import Command
from config_reader import config
from aiogram.utils.keyboard import InlineKeyboardBuilder

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    kb = [
        
        [types.KeyboardButton(text= 'Запись на сеанс')],
        [types.KeyboardButton(text= 'Выбор (салона, офиса, и т.д.)')],
        [types.KeyboardButton(text= 'Выбор исполнителя')],
        [types.KeyboardButton(text= 'Просмотр текущих записей')]
        
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        #resize_keyboard = True,
        input_field_placeholder='выберите нужную вам функцию'
    )
    
    await message.answer('Привет я личный секретарь (Имя владельца), я помогу вам с записью на нужные вам сеанссы', reply_markup=keyboard)

@dp.message(F.text.lower() == 'запись на сеанс')
async def with_puree(message: types.Message):
    bilder = InlineKeyboardBuilder()
    bilder.add(types.InlineKeyboardButton(
        text='14.04',
        callback_data='session_date')
    )
    await message.answer(
        'Выбирите дату на которое планируете записатся',
        reply_markup=bilder.as_markup()
        )
@dp.callback_query(F.data == 'session_date')
async def send_session_date(callback: types.CallbackQuery):
    await callback.message.answer(str('Вы успешно записаны на данное число, информация о вашей записе переданна (исполнителю, мастеру и т.д.)'))


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
# Fuck