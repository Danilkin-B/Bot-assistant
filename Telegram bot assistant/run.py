import asyncio # для асинхронности
import logging # логирование 
from aiogram import Bot, Dispatcher

from app.handlers import router


async def main():
    bot = Bot(token='')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot) # Передаём ботов


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO) # Логирование
    try:

        asyncio.run(main())
    except KeyboardInterrupt: # защита от Ctrl + C
        print('Error')