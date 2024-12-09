# Он мне ответил!

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api=''
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

# Обработчик всех остальных сообщений
@dp.message_handler(lambda message: True)
async def all_messages(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

