import asyncio
import logging

from aiogram import Bot, Dispatcher
from handlers import other_handlers, user_handlers

logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    BOT_TOKEN = '6419228214:AAGGnk5FYBiuat3dI8CAk_6Rr1z1kDgNqZk'

    # Инициализируем бот и диспетчер
    bot = Bot(token=BOT_TOKEN,
              parse_mode='HTML')
    dp = Dispatcher()

    # Регистриуем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
