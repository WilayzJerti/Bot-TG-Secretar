# Version: Alpha 0.0.9
import asyncio
import logging

from aiogram import F, Bot, Dispatcher, types, executor
from aiogram.filters.command import Command
from config_reader import config
from aiogram.utils.keyboard import InlineKeyboardBuilder
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from aiogram.contrib.fsm_storage.memory import MemoryStorage 

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()

user_data = {} # Здесь хранятся пользоватьльские данные
user_data_time = {}
user_data_performer = {}
user_data_entry = {}

@dp.message(Command('start')) 
async def cmd_start(message: types.Message):
    kb = [
        
        [types.KeyboardButton(text= 'Запись на сеанс📔')],
        [types.KeyboardButton(text= 'Выбор исполнителя🧑‍💻')],
        [types.KeyboardButton(text= 'Просмотр текущих записей📆')]
        
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        #resize_keyboard = True,
        input_field_placeholder='выберите нужную вам функцию'
    )
    
    await message.answer('Привет я личный секретарь (Имя владельца), я помогу вам с записью на нужные вам сеанссы', reply_markup=keyboard) # Приветсвеное сообщение при запуске бота 

def get_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(text='20.05', callback_data='session_One'),
            types.InlineKeyboardButton(text='21.05', callback_data='session_Two'),
            types.InlineKeyboardButton(text='22.05', callback_data='session_Three'),
            types.InlineKeyboardButton(text='23.05', callback_data='session_Four')
        ],
        [
            types.InlineKeyboardButton(text='24.05', callback_data='session_Five'),
            types.InlineKeyboardButton(text='25.05', callback_data='session_Six'),
            types.InlineKeyboardButton(text='26.05', callback_data='session_Seven'),
            types.InlineKeyboardButton(text='27.05', callback_data='session_Eight')
        ],
        [
            types.InlineKeyboardButton(text='28.05', callback_data='session_Nine'),
            types.InlineKeyboardButton(text='29.05', callback_data='session_Ten'),
            types.InlineKeyboardButton(text='30.05', callback_data='session_Eleven'),
            types.InlineKeyboardButton(text='31.05', callback_data='session_Twelve')
        ],
        [types.InlineKeyboardButton(text="Подтвердить", callback_data="session_end")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def get_keyboard_time():
    buttons = [
        [
            types.InlineKeyboardButton(text='12:00', callback_data='time_Onen'),
            types.InlineKeyboardButton(text='14:00', callback_data='time_Twon'),
            types.InlineKeyboardButton(text='16:00', callback_data='time_Threen')
        ],
        [
            types.InlineKeyboardButton(text='16:30', callback_data='time_Fourn'),
            types.InlineKeyboardButton(text='18:00', callback_data='time_Fiven'),
            types.InlineKeyboardButton(text='21:45', callback_data='time_Sixn')
        ],
        [types.InlineKeyboardButton(text="Подтвердить", callback_data="time_endn")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

async def update_ses_text(message: types.Message, new_value: str):
    await message.edit_text(
        f'Выберете, на какую дату вы хотите записаться. Выбранная дата:{new_value}',
        reply_markup=get_keyboard()
    )

@dp.message(F.text.lower() == 'запись на сеанс📔')
async def callback_ses(message: types.Message):
    user_data[message.from_user.id] = '0'
    await message.answer('Выберете, на какую дату вы хотите записаться. Выбранная дата: 00.00', reply_markup=get_keyboard())


@dp.callback_query(F.data.startswith('session_'))
async def callbacks_ses(callback: types.CallbackQuery):
    user_value = user_data.get(callback.from_user.id, '0')
    action = callback.data.split("_")[1]

    if action == "One":
        user_data[callback.from_user.id] = user_value = '20.05'
        await update_ses_text(callback.message, new_value = '20.05')
    elif action == "Two":
        user_data[callback.from_user.id] = user_value ='21.05'
        await update_ses_text(callback.message, new_value = '21.05')
    elif action == "Three":
        user_data[callback.from_user.id] = user_value ='22.05'
        await update_ses_text(callback.message, new_value = '22.05')
    elif action == "Four":
        user_data[callback.from_user.id] = user_value ='23.05'
        await update_ses_text(callback.message, new_value = '23.05')
    elif action == "Five":
        user_data[callback.from_user.id] = user_value ='24.05'
        await update_ses_text(callback.message, new_value = '24.05')
    elif action == "Six":
        user_data[callback.from_user.id] = user_value ='25.05'
        await update_ses_text(callback.message, new_value = '25.05')
    elif action == "Seven":
        user_data[callback.from_user.id] = user_value ='26.05'
        await update_ses_text(callback.message, new_value = '26.05')
    elif action == "Eight":
        user_data[callback.from_user.id] = user_value ='27.05'
        await update_ses_text(callback.message, new_value = '27.05')
    elif action == "Nine":
        user_data[callback.from_user.id] = user_value ='28.05'
        await update_ses_text(callback.message, new_value = '28.05')
    elif action == "Ten":
        user_data[callback.from_user.id] = user_value ='29.05'
        await update_ses_text(callback.message, new_value = '29.05')
    elif action == "Eleven":
        user_data[callback.from_user.id] = user_value ='30.05'
        await update_ses_text(callback.message, new_value = '30.05')
    elif action == "Twelve":
        user_data[callback.from_user.id] = user_value ='31.05'
        await update_ses_text(callback.message, new_value = '31.05')    
    elif action == "end":
        await callback.message.edit_text(f"На данное число ({user_value}) свободны такие окна.", reply_markup=get_keyboard_time())
        async def callback_ses_time(message: types.Message):
                user_data_time[message.from_user.id] = '0'
                await message.answer('Выбраное время: 00:00', reply_markup=get_keyboard_time())
            
        async def update_ses_time_text(message: types.Message, user_new_time: str):
            await message.edit_text(
                f'Выбраное время:{user_new_time}',
                reply_markup=get_keyboard_time()
    )
        
        @dp.callback_query(F.data.startswith('time_'))
        async def callbacks_ses_time(callback: types.CallbackQuery):
            user_time = user_data_time.get(callback.from_user.id, '0')
            action = callback.data.split("_")[1]

            if action == "Onen":
                user_data_time[callback.from_user.id] = user_time = '12:00'
                await update_ses_time_text(callback.message, user_new_time = '12:00')
            elif action == "Twon":
                user_data_time[callback.from_user.id] = user_time ='14:00'
                await update_ses_time_text(callback.message, user_new_time = '14:00')
            elif action == "Threen":
                user_data_time[callback.from_user.id] = user_time ='16:00'
                await update_ses_time_text(callback.message, user_new_time = '16:00')
            elif action == "Fourn":
                user_data_time[callback.from_user.id] = user_time ='16:30'
                await update_ses_time_text(callback.message, user_new_time = '16:30')
            elif action == "Fiven":
                user_data_time[callback.from_user.id] = user_time ='18:00'
                await update_ses_time_text(callback.message, user_new_time = '18:00')
            elif action == "Sixn":
                user_data_time[callback.from_user.id] = user_time ='21:45'
                await update_ses_time_text(callback.message, user_new_time = '21:45')  
            elif action == "endn":
                await callback.message.edit_text(f"Вы успешно записались: Дата {user_value} Время {user_time}")
                
                await callback.answer()
                
    await callback.answer()

def get_keyboard_performer():
    buttons = [
        [
            types.InlineKeyboardButton(text='Исполнитель №1', callback_data='performer_One'),
            types.InlineKeyboardButton(text='Исполнитель №2', callback_data='performer_Two')
        ],
        [
            types.InlineKeyboardButton(text='Исполнитель №3', callback_data='performer_Three'),
            types.InlineKeyboardButton(text='Исполнитель №4', callback_data='performer_Four')
        ],
        [types.InlineKeyboardButton(text="Подтвердить", callback_data="performer_end")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

async def update_per_text(message: types.Message, new_text: str):
    await message.edit_text(
        f'Выберете (мастера, исполнителя и т.д.) к которому хотите записаться на сеанс. Выбраный исполнитель:{new_text}',
        reply_markup=get_keyboard_performer()
    )

@dp.message(F.text.lower() == 'выбор исполнителя🧑‍💻')
async def callback_per(message: types.Message):
    user_data_performer[message.from_user.id] = '0'
    await message.answer('Выберете (мастера, исполнителя и т.д.) к которому хотите записаться на сеанс. Выбраный исполнитель: - - -', reply_markup=get_keyboard_performer())

@dp.callback_query(F.data.startswith('performer_'))
async def callbacks_per(callback: types.CallbackQuery):
    user_performer = user_data_performer.get(callback.from_user.id, '0')
    action = callback.data.split("_")[1]

    if action == "One":
        user_data_performer[callback.from_user.id] = user_performer = 'Исполнитель №1'
        await update_per_text(callback.message, new_text = 'Исполнитель №1')
    elif action == "Two":
        user_data_performer[callback.from_user.id] = user_performer ='Исполнитель №2'
        await update_per_text(callback.message, new_text = 'Исполнитель №2')
    elif action == "Three":
        user_data_performer[callback.from_user.id] = user_performer ='Исполнитель №3'
        await update_per_text(callback.message, new_text = 'Исполнитель №3')
    elif action == "Four":
        user_data_performer[callback.from_user.id] = user_performer ='Исполнитель №4'
        await update_per_text(callback.message, new_text = 'Исполнитель №4')  
    elif action == "end":
        await callback.message.edit_text(f"Выбраный исполнитель: ({user_performer})")
        
        await callback.answer()

@dp.message(F.text.lower() == 'просмотр текущих записей📆')
async def callbacks_per(message: types.Message):
    user_data_entry[message.from_user.id] = '0'
    await message.answer(F'Вы записаны на {user_data} в {user_data_time} к {user_data_performer}')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())