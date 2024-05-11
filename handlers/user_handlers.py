from aiogram import F, Router
from aiogram.filters import Command, CommandStart, BaseFilter
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.keyboards import Start_board, adm_kb, nex_kb, send_kb
from lexicon.lexicon_ru import LEXICON_RU
from BaseD.sqbd import get_ank
from aiogram.utils.formatting import Text, Bold
from BaseD.sqbd import add_new_ank
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

# Инициализируем роутер уровня модуля
router = Router()

admin_ids: list[int] = [6153194013]


class adank(StatesGroup):
    FIO = State()
    Educat = State()
    Profes = State()
    like = State()
    Experience = State()
    Qualit = State()
    Languag = State()
    Info = State()
    Works = State()
    Contacts = State()


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
                         reply_markup=Start_board
                         )


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'],
                         reply_markup=Start_board
                         )


@router.message(F.text == LEXICON_RU['all_ank'], IsAdmin(admin_ids))
async def process_viev(message: Message):
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


@router.message(F.text == LEXICON_RU['add_ank'])
async def Step_one(message: Message, state: FSMContext):
    await state.set_state(adank.FIO)
    await message.answer(
        text='Ввидите ваше ФИО.'
    )


@router.message(adank.FIO)
async def Step_two(message: Message, state: FSMContext):
    await state.update_data(FIO=message.text)
    await state.set_state(adank.Educat)
    await message.answer(
        text='Ввидите полученое вами образование.'
    )


@router.message(adank.Educat)
async def Step_three(message: Message, state: FSMContext):
    await state.update_data(Educat=message.text)
    await state.set_state(adank.Profes)
    await message.answer(
        text='Ввидите полученое вами профессию.'
    )


@router.message(adank.Profes)
async def Step_four(message: Message, state: FSMContext):
    await state.update_data(Profes=message.text)
    await state.set_state(adank.like)
    await message.answer(
        text='Ввидите желаемую должность.'
    )


@router.message(adank.like)
async def Step_five(message: Message, state: FSMContext):
    await state.update_data(like=message.text)
    await state.set_state(adank.Experience)
    await message.answer(
        text='Ввидите ваш опыт работы. (если его нету введите "-")'
    )


@router.message(adank.Experience)
async def Step_six(message: Message, state: FSMContext):
    await state.update_data(Experience=message.text)
    await state.set_state(adank.Qualit)
    await message.answer(
        text='Ввидите ваши качества.'
    )


@router.message(adank.Qualit)
async def Step_seven(message: Message, state: FSMContext):
    await state.update_data(Qualit=message.text)
    await state.set_state(adank.Languag)
    await message.answer(
        text='Ввидите языки которые вы знаете.'
    )


@router.message(adank.Languag)
async def Step_eght(message: Message, state: FSMContext):
    await state.update_data(Languag=message.text)
    await state.set_state(adank.Info)
    await message.answer(
        text='Ввидите информацию о себе.'
    )


@router.message(adank.Info)
async def Step_nine(message: Message, state: FSMContext):
    await state.update_data(Info=message.text)
    await state.set_state(adank.Works)
    await message.answer(
        text='Ввидите ссылки на ваши работы через пробел. (если их нету введите "-")'
    )


@router.message(adank.Works)
async def Step_ten(message: Message, state: FSMContext):
    await state.update_data(Works=message.text)
    await state.set_state(adank.Contacts)
    await message.answer(
        text='Ввидите номер телефона и почту. (Пример: +7********** *****@****.***)'
    )


@router.message(adank.Contacts)
async def Step_elev(message: Message, state: FSMContext):
    await state.update_data(Contact=message.text)
    data = await state.get_data()
    await message.answer(
        text=f'Спасибо за резюме. Я его вам выведу: \n ФИО: {data['FIO']} \n Образование: {data['Educat']} \n'
             f' Профессия: {data['Profes']} \n Желаемая должность: {data['like']} \n Опыт: {data['Experience']} \n'
             f' Качества: {data['Qualit']} \n Языки: {data['Languag']} \n Информация: {data['Info']} \n'
             f' Примеры работ: {data['Works']} \n Контактная информация: {data['Contact']}'
    )
    await state.clear()
