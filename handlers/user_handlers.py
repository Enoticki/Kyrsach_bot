from aiogram import F, Router
from aiogram.filters import Command, CommandStart, BaseFilter
from aiogram.types import Message
from keyboards.keyboards import Start_board, adm_kb
from lexicon.lexicon_ru import LEXICON_RU
from BaseD.sqbd import get_ank
from aiogram.utils.formatting import Text, Bold

# Инициализируем роутер уровня модуля
router = Router()

admin_ids: list[int] = [6153194013]


class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    content = Text(
        "Привет, ",
        Bold(message.from_user.full_name),
        ", я помогу тебе в составлении резюме!"
    )
    await message.answer(
        **content.as_kwargs()
    )
    await message.answer(text=LEXICON_RU['/start'],
                         reply_markup=Start_board)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'],
                         reply_markup=Start_board)


@router.message(F.text == LEXICON_RU['add_ank'])
async def process_add(message: Message):
    await message.answer(
        text='Ввидите ваше ФИО',
    )


@router.message(F.text == LEXICON_RU['all_ank'], IsAdmin(admin_ids))
async def process_add(message: Message):
    Ank = await get_ank()
    users_str = "\n".join([str(anke) for anke in Ank])
    if not Ank:
        await message.answer(
            text='Рузюме сейчас нету'
        )
    else:
        await message.answer(
            text=f'Здраствуйте админстратор сейчас я выведу все резюме!',
            reply_markup=adm_kb
        )
        await message.answer(users_str)
