from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from BaseD.request import viev_all, Find_by_id
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
button_5 = KeyboardButton(text=LEXICON_RU['find by Qualities'])
button_6 = KeyboardButton(text=LEXICON_RU['inform'])
button_7 = KeyboardButton(text=LEXICON_RU['home'])

adm_kb = ReplyKeyboardMarkup(
    keyboard=[[button_0, button_1],
              [button_2, button_3],
              [button_4, button_5],
              [button_6, button_7]],
    resize_keyboard=True
)


async def all_vievs():
    All = await viev_all()
    keyboard = InlineKeyboardBuilder()
    for viev in All:
        keyboard.add(InlineKeyboardButton(text=viev.FIO, callback_data=f'FIO_{viev.iad}'))
    return keyboard.adjust(2).as_markup()


async def id():
    All = await Find_by_id()
    keyboard = InlineKeyboardBuilder()
    for viev in All:
        keyboard.add(InlineKeyboardButton(text=viev.FIO, callback_data=f'ID_{viev.iad}'))
    return keyboard.adjust(2).as_markup()

button_8 = KeyboardButton(text=LEXICON_RU['All help'])
button_9 = KeyboardButton(text=LEXICON_RU['find by FIO help'])
button_10 = KeyboardButton(text=LEXICON_RU['find by id help'])
button_11 = KeyboardButton(text=LEXICON_RU['find by profession help'])
button_12 = KeyboardButton(text=LEXICON_RU['find by Languages help'])
button_13 = KeyboardButton(text=LEXICON_RU['find by Qualities help'])

adm_kb_help = ReplyKeyboardMarkup(
    keyboard=[[button_8, button_9],
              [button_10, button_11],
              [button_12, button_13],
              [button_7]],
    resize_keyboard=True
)
