from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import sqlite3

# Создаем подключение к базе данных (файл my_database.db будет создан)
connection = sqlite3.connect('Users.db')
cursor = connection.cursor()

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = '6419228214:AAGGnk5FYBiuat3dI8CAk_6Rr1z1kDgNqZk'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)
    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER
    )
    ''')

    cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser', 'newuser@example.com', 28))
    # Выбираем всех пользователей
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()

    # Выводим результаты
    for user in users:
        await user

    # Закрываем соединение
    connection.close()


if __name__ == '__main__':
    dp.run_polling(bot)

cursor.execute('INSERT INTO Users_ank (username, email, age) VALUES (?, ?, ?)', ('newuser', 'newuser@example.com', 28))

connection.close()
