import asyncio  # Работа с асинхронностью

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command,Text  # Фильтр для /start, /...
from aiogram.types import Message , ContentType,BotCommand  # Тип сообщения

import AI
from config import config  # Config

API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()  # Менеджер бота


# dp.message - обработка сообщений
# Command(commands=['start'] Фильтр для сообщений, берём только /start
@dp.message(Command(commands=['start']))  # Берём только сообщения, являющиеся командой /start
async def start_command(message: Message):  # message - сообщение, которое прошло через фильтр
    await message.answer("Привет!задай свой вопрос,а я с помощью магического шара скажу тебе ответ)")  # Отвечаем на полученное сообщени

@dp.message(Command(commands='help'))
async def handle_help(message: Message):
    await message.answer('* типа я тебе помогаю*')

@dp.message(Command('delete_menu'))
async def handle_menu_delete(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer('Вы удалили меню,зачем?(((')

@dp.message(Command(commands='menu'))
async def handle_help(message: Message):
    await message.answer('вы открыли менюшку*типа меню*')

@dp.message()
async def do_answer(message:Message):
    answer = AI.generate_answer()
    if answer:
        await message.answer(answer)


async def main():
    try:
        print('Bot Started')
        await dp.start_polling(bot)
    finally:
        await bot.session.close()





if __name__ == '__main__':  # Если мы запускаем конкретно этот файл.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')

