from aiogram import Router
from keyboards.keyboards import Start_board
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

# Инициализируем роутер уровня модуля
router = Router()


# Этот хэндлер будет срабатывать на любые ваши сообщения,
@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'],
                         reply_markup=Start_board
                         )
