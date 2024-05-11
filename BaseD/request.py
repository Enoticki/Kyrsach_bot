from BaseD.sqbd import async_session
from BaseD.sqbd import User
from sqlalchemy import select


async def add_new_ank(FIO, Educat, Profes, like, Experience, Qualit, Languag, Info, Works, Contacts):
    async with async_session() as session:
        session.add(User(FIO=FIO, Educat=Educat, Profes=Profes, like=like, Experience=Experience,
                         Qualit=Qualit, Languag=Languag, Info=Info, Works=Works, Contacts=Contacts))
        await session.commit()


async def viev_all():
    async with async_session() as session:
        return await session.scalars(select(User))


async def get_ank(id_ank):
    async with async_session() as session:
        return await session.scalar(select(User).where(User.id == id_ank))
