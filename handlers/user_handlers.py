from aiogram import F, Router
from aiogram.filters import Command, CommandStart, BaseFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.utils.formatting import Text, Bold

from BaseD.States import Adank, find
from BaseD.request import *
from keyboards.keyboards import *
from lexicon.lexicon_ru import LEXICON_RU

# Инициализируем роутер уровня модуля
router = Router()

admin_ids: list[int] = [6153194013, 1067952654]


class IsAdmin(BaseFilter):
    def __init__(self, Admin_ids: list[int]) -> None:
        self.admin_ids = Admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    content = Text(
        "Привет, ",
        Bold(message.from_user.full_name),
        ", я помогу тебе в составлении резюме!\n"
        "Резюме можно сделать всего один раз!"
    )
    await message.answer(
        **content.as_kwargs()
    )
    await message.answer(
        text=LEXICON_RU['/start'],
        reply_markup=Start_board
    )


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/help'],
        reply_markup=Start_board
    )


@router.message(F.text == LEXICON_RU['inform'])
async def process_viev(message: Message):
    await message.answer(
        text=f'Не понимаете как работает поиск.\n Выберите способ я расскажу подробнее о нём!',
        reply_markup=adm_kb_help
    )


@router.message(F.text == LEXICON_RU['find by FIO help'])
async def process_viev(message: Message):
    await message.answer(
        text=f'Введите ФИ или ФИО человека как указано в анкете, например: Дзюба Максим или Илькаев Наиль Рауфович. ',
        reply_markup=adm_kb_help
    )


@router.message(F.text == LEXICON_RU['find by id help'])
async def process_viev(message: Message):
    await message.answer(
        text=f'Выводит последние 2 анкеты которые оставили пользователи.',
        reply_markup=adm_kb_help
    )


@router.message(F.text == LEXICON_RU['find by profession help'])
async def process_viev(message: Message):
    await message.answer(
        text=f'Введите профессию которую хотите найти например: Программист или Уборщик.',
        reply_markup=adm_kb_help
    )


@router.message(F.text == LEXICON_RU['find by Languages help'])
async def process_viev(message: Message):
    await message.answer(
        text=f'Введите язык который должен знать человек например: Русский или Английский.',
        reply_markup=adm_kb_help
    )


@router.message(F.text == LEXICON_RU['find by Qualities help'])
async def process_viev(message: Message):
    await message.answer(
        text=f'Введите качества человека например: Коммуникабельность или Обучаемость.',
        reply_markup=adm_kb_help
    )


@router.message(F.text == LEXICON_RU['All help'])
async def process_viev(message: Message):
    await message.answer(
        text=f'Показывает все анкеты которые есть на данный момент.',
        reply_markup=adm_kb_help
    )


@router.message(F.text == LEXICON_RU['all_ank'], IsAdmin(admin_ids))
async def process_viev(message: Message):
    await message.answer(
        text=f'Здраствуйте админстратор выберите способ поиска!',
        reply_markup=adm_kb
    )


@router.message(F.text == LEXICON_RU['All'])
async def process_all(message: Message):
    await message.answer(
        text=f'Администратор вот все анкеты, выберите анкету.',
        reply_markup=await all_vievs()
    )


@router.callback_query(F.data.startswith('FIO_'))
async def process_men(callback: CallbackQuery):
    ank_data = await get_ank(callback.data.split('_')[1])
    await callback.answer('Вы выбрали анкету')
    await callback.message.answer(
        text=f'\n ФИО: {ank_data.FIO} \n Образование: {ank_data.Educat} \n'
             f' Профессия: {ank_data.Profes} \n Желаемая должность: {ank_data.like} \n Опыт: {ank_data.Experience} \n'
             f' Качества: {ank_data.Qualit} \n Языки: {ank_data.Languag} \n Языки программирования: {ank_data.Komplang}'
             f' \n Информация: {ank_data.Info} \n Примеры работ: {ank_data.Works}'
             f' \n Контактная информация: {ank_data.Contacts}',
        reply_markup=adm_kb
    )


@router.message(F.text == LEXICON_RU['find by FIO'])
async def process_FIO(message: Message, state: FSMContext):
    await state.set_state(find.FIO)
    await message.answer(
        text='Введите ФИО кого нужно найти.'
    )


@router.message(find.FIO)
async def find_FIO(message: Message, state: FSMContext):
    ank_data = await Find_by_FIO(message.text)
    await message.answer(
        text=f'\n ФИО: {ank_data.FIO} \n Образование: {ank_data.Educat} \n'
             f' Профессия: {ank_data.Profes} \n Желаемая должность: {ank_data.like} \n Опыт: {ank_data.Experience} \n'
             f' Качества: {ank_data.Qualit} \n Языки: {ank_data.Languag} \n Языки программирования: {ank_data.Komplang}'
             f' \n Информация: {ank_data.Info} \n Примеры работ: {ank_data.Works}'
             f' \n Контактная информация: {ank_data.Contacts}',
    )
    await state.clear()


@router.message(F.text == LEXICON_RU['find by id'])
async def process_all(message: Message):
    await message.answer(
        text='Вот самые новые анкеты!',
        reply_markup=await iad()
    )


@router.callback_query(F.data.startswith('ID_'))
async def process_men(callback: CallbackQuery):
    ank_data = await get_ank(callback.data.split('_')[1])
    await callback.answer('Вы выбрали анкету')
    await callback.message.answer(
        text=f'\n ФИО: {ank_data.FIO} \n Образование: {ank_data.Educat} \n'
             f' Профессия: {ank_data.Profes} \n Желаемая должность: {ank_data.like} \n Опыт: {ank_data.Experience} \n'
             f' Качества: {ank_data.Qualit} \n Языки: {ank_data.Languag} \n Языки программирования: {ank_data.Komplang}'
             f' \n Информация: {ank_data.Info} \n Примеры работ: {ank_data.Works}'
             f' \n Контактная информация: {ank_data.Contacts}',
        reply_markup=adm_kb
    )


@router.message(F.text == LEXICON_RU['find by profession'])
async def process_profession(message: Message, state: FSMContext):
    await state.set_state(find.profession)
    await message.answer(
        text='Введите нужную профессию.'
    )


@router.message(find.profession)
async def find_profession(message: Message, state: FSMContext):
    ank_data = await Find_by_prof(message.text)
    await message.answer(
        text=f'\n ФИО: {ank_data.FIO} \n Образование: {ank_data.Educat} \n'
             f' Профессия: {ank_data.Profes} \n Желаемая должность: {ank_data.like} \n Опыт: {ank_data.Experience} \n'
             f' Качества: {ank_data.Qualit} \n Языки: {ank_data.Languag} \n Языки программирования: {ank_data.Komplang}'
             f' \n Информация: {ank_data.Info} \n Примеры работ: {ank_data.Works}'
             f' \n Контактная информация: {ank_data.Contacts}',
    )
    await state.clear()


@router.message(F.text == LEXICON_RU['find by Languages'])
async def process_Languages(message: Message, state: FSMContext):
    await state.set_state(find.Languages)
    await message.answer(
        text='Введите языки которые должен знать работик.'
    )


@router.message(find.Languages)
async def find_lang(message: Message, state: FSMContext):
    ank_data = await Find_by_lang(message.text)
    await message.answer(
        text=f'\n ФИО: {ank_data.FIO} \n Образование: {ank_data.Educat} \n'
             f' Профессия: {ank_data.Profes} \n Желаемая должность: {ank_data.like} \n Опыт: {ank_data.Experience} \n'
             f' Качества: {ank_data.Qualit} \n Языки: {ank_data.Languag} \n Языки программирования: {ank_data.Komplang}'
             f' \n Информация: {ank_data.Info} \n Примеры работ: {ank_data.Works}'
             f' \n Контактная информация: {ank_data.Contacts}',
    )
    await state.clear()


@router.message(F.text == LEXICON_RU['find by Qualities'])
async def process_experience(message: Message, state: FSMContext):
    await state.set_state(find.Qualities)
    await message.answer(
        text='Введите личностные качества которые должены быть у работника.'
    )


@router.message(find.Qualities)
async def find_qual(message: Message, state: FSMContext):
    ank_data = await Find_by_qual(message.text)
    await message.answer(
        text=f'\n ФИО: {ank_data.FIO} \n Образование: {ank_data.Educat} \n'
             f' Профессия: {ank_data.Profes} \n Желаемая должность: {ank_data.like} \n Опыт: {ank_data.Experience} \n'
             f' Качества: {ank_data.Qualit} \n Языки: {ank_data.Languag} \n Языки программирования: {ank_data.Komplang}'
             f' \n Информация: {ank_data.Info} \n Примеры работ: {ank_data.Works}'
             f' \n Контактная информация: {ank_data.Contacts}',
    )
    await state.clear()


@router.message(F.text == LEXICON_RU['inform'])
async def process_all(message: Message):
    await message.answer(
        text=f'Здесь вы можете узнать как пользоваться какой либо функцией',
        # reply_markup=
    )


@router.message(F.text == LEXICON_RU['home'])
async def process_all(message: Message):
    await message.answer(
        text=f'Вы вернулись в начало',
        reply_markup=Start_board
    )


@router.message(F.text == LEXICON_RU['add_ank'])
async def Step_one(message: Message, state: FSMContext):
    await state.set_state(Adank.FIO)
    await message.answer(
        text='Введите ваше ФИО.'
    )


@router.message(Adank.FIO)
async def Step_two(message: Message, state: FSMContext):
    await state.update_data(FIO=message.text)
    await state.set_state(Adank.Educat)
    await message.answer(
        text='Введите полученое вами образование. (Каждое образование с большой буквы.)'
    )


@router.message(Adank.Educat)
async def Step_three(message: Message, state: FSMContext):
    await state.update_data(Educat=message.text)
    await state.set_state(Adank.Profes)
    await message.answer(
        text='Введите полученые вами профессии. (Каждую профессию с большой буквы.)'
    )


@router.message(Adank.Profes)
async def Step_four(message: Message, state: FSMContext):
    await state.update_data(Profes=message.text)
    await state.set_state(Adank.like)
    await message.answer(
        text='Введите желаемую должность. (Каждую должность с большой буквы.)'
    )


@router.message(Adank.like)
async def Step_five(message: Message, state: FSMContext):
    await state.update_data(like=message.text)
    await state.set_state(Adank.Experience)
    await message.answer(
        text='Введите ваш опыт работы. (если его нету введите "-")'
    )


@router.message(Adank.Experience)
async def Step_six(message: Message, state: FSMContext):
    await state.update_data(Experience=message.text)
    await state.set_state(Adank.Qualit)
    await message.answer(
        text='Введите ваши качества. (Каждое качество с большой буквы.)'
    )


@router.message(Adank.Qualit)
async def Step_seven(message: Message, state: FSMContext):
    await state.update_data(Qualit=message.text)
    await state.set_state(Adank.Languag)
    await message.answer(
        text='Введите языки на которых вы разговариваете. (Каждый языки с большой буквы.)'
    )


@router.message(Adank.Languag)
async def Step_eght(message: Message, state: FSMContext):
    await state.update_data(Languag=message.text)
    await state.set_state(Adank.Сomplang)
    await message.answer(
        text='Введите языки программирования которые вы знаете. (если их нету введите "-",'
             ' каждый язык с большой буквы.)'
    )


@router.message(Adank.Сomplang)
async def Step_eghtfive(message: Message, state: FSMContext):
    await state.update_data(Сomplang=message.text)
    await state.set_state(Adank.Info)
    await message.answer(
        text='Введите информацию о себе.'
    )


@router.message(Adank.Info)
async def Step_nine(message: Message, state: FSMContext):
    await state.update_data(Info=message.text)
    await state.set_state(Adank.Works)
    await message.answer(
        text='Введите ссылки на ваши работы через пробел. (если их нету введите "-")'
    )


@router.message(Adank.Works)
async def Step_ten(message: Message, state: FSMContext):
    await state.update_data(Works=message.text)
    await state.set_state(Adank.Contacts)
    await message.answer(
        text='Введите номер телефона и почту. (Пример: +7********** *****@****.***)'
    )


@router.message(Adank.Contacts)
async def Step_elev(message: Message, state: FSMContext):
    await state.update_data(Contact=message.text)
    data = await state.get_data()
    await message.answer(
        text=f'Спасибо за резюме. Я его вам выведу: \n ФИО: {data['FIO']} \n Образование: {data['Educat']} \n'
             f' Профессия: {data['Profes']} \n Желаемая должность: {data['like']} \n Опыт: {data['Experience']} \n'
             f' Качества: {data['Qualit']} \n Языки: {data['Languag']} \n Языки программирования {data['Сomplang']}'
             f' \n Информация: {data['Info']} \n Примеры работ: {data['Works']}'
             f' \n Контактная информация: {data['Contact']}'
    )
    await add_new_ank(data['FIO'], data['Educat'], data['Profes'], data['like'], data['Experience'],
                      data['Qualit'], data['Languag'], data['Сomplang'], data['Info'], data['Works'], data['Contact'],
                      message.from_user.id)
    await OnePhase(message.from_user.id, data['FIO'])
    await state.clear()
