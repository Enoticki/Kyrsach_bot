from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, BaseFilter, Command
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from BaseD import sqbd

BOT_TOKEN = '6419228214:AAGGnk5FYBiuat3dI8CAk_6Rr1z1kDgNqZk'

# Инициализируем бот и диспетчер
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def on_starup(_):
    await sqbd.db_connect()
    print("Подключение к бд успешно")


adm_id = sqbd.get_adm()


class IsAdmin(BaseFilter):

    def __init__(self, admin_ids: list[int]) -> None:
        # В качестве параметра фильтр принимает список с целыми числами
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids


button_1 = KeyboardButton(text='Создать анкету')
button_2 = KeyboardButton(text='Просмотреть анкеты', callback_data='get_ank')

keyboard = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]])


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        'Привет будущий трудяга! \n'
        'Здесь ты можешь оставить свою анкету для нахождения работы',
        reply_markup=keyboard
    )


@dp.message(F.text == 'Создать анкету')
async def process_add(message: Message):
    await message.answer(
        text='Да, несомненно, кошки боятся собак. '
             'Но вы видели как они боятся огурцов?',
        reply_markup=ReplyKeyboardRemove()
    )


@dp.message(F.text == 'Просмотреть анкеты')
async def process_add(message: Message):
    adm_id = await sqbd.get_adm()
    if IsAdmin(adm_id):
        await message.answer(
            text='Да, несомненно, кошки боятся собак. '
                 'Но вы видели как они боятся огурцов?',
            reply_markup=ReplyKeyboardRemove()
        )
    else:
        await message.answer(
            text='У вас недостаточно прав для этого действия'
                 'обратитесь к администратору или создайте анкету'
        )


if __name__ == '__main__':
    dp.run_polling(bot)
