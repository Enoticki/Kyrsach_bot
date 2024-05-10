from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

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

adm_kb = ReplyKeyboardMarkup(
    keyboard=[[button_0],
              [button_1],
              [button_2],
              [button_3],
              [button_4],
              [button_5],
              [button_6]],
    resize_keyboard=True
)