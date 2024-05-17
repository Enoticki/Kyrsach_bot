from aiogram.fsm.state import StatesGroup, State


# noinspection NonAsciiCharacters
class Adank(StatesGroup):
    FIO = State()
    Educat = State()
    Profes = State()
    like = State()
    Experience = State()
    Qualit = State()
    Languag = State()
    Сomplang = State()
    Info = State()
    Works = State()
    Contacts = State()


class find(StatesGroup):
    FIO = State()
    id = State()
    profession = State()
    Languages = State()
    experience = State()
    Qualities = State()
