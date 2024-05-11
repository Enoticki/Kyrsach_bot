from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from BaseD.request import viev_all
from lexicon.lexicon_ru import LEXICON_RU

Add = KeyboardButton(text=LEXICON_RU['add_ank'])
View = KeyboardButton(text=LEXICON_RU['all_ank'])

Start_board_builder = ReplyKeyboardBuilder()

Start_board_builder.row(Add, View)

Start_board: ReplyKeyboardMarkup = Start_board_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# Создаем кнопки администратора
button_0 = KeyboardButton(text=LEXICON_RU['All'])
button_1 = KeyboardButton(text=LEXICON_RU['find by FIO'])
button_2 = KeyboardButton(text=LEXICON_RU['find by id'])
button_3 = KeyboardButton(text=LEXICON_RU['find by profession'])
button_4 = KeyboardButton(text=LEXICON_RU['find by Languages'])
button_5 = KeyboardButton(text=LEXICON_RU['find by experience'])
button_6 = KeyboardButton(text=LEXICON_RU['find by Qualities'])
button_7 = KeyboardButton(text=LEXICON_RU['home'])

adm_kb = ReplyKeyboardMarkup(
    keyboard=[[button_0],
              [button_1],
              [button_2],
              [button_3],
              [button_4],
              [button_5],
              [button_6],
              [button_7]],
    resize_keyboard=True
)

# Создаем кнопку далее
nex = KeyboardButton(text=LEXICON_RU['next'])

nex_kb = ReplyKeyboardMarkup(
    keyboard=[[nex]],
    resize_keyboard=True
)

# Создаем кнопку отправить
send = KeyboardButton(text=LEXICON_RU['send'])

send_kb = ReplyKeyboardMarkup(
    keyboard=[[send]],
    resize_keyboard=True
)

async def all_vievs():
    all = await viev_all()
    keyboard = InlineKeyboardBuilder()
    for viev in all:
        keyboard.add(InlineKeyboardButton(text=viev.FIO, callback_data=viev.id))
    keyboard.add(InlineKeyboardButton(text=LEXICON_RU['home']))
    return keyboard.adjust(4).as_markup()

