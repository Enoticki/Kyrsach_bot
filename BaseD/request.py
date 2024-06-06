from sqlalchemy import select, BigInteger, desc

from BaseD.sqbd import User_Info, User_name
from BaseD.sqbd import async_session


async def add_new_ank(FIO, Educat, Profes, like, Experience, Qualit, Languag, Сomplang, Info, Works, Contacts,
                      tg_id: BigInteger):
    async with async_session() as session:
        user = await session.scalar(select(User_name).where(User_name.tg_id == tg_id))

        if user is not User_name:
            session.add(User_Info(FIO=FIO, Educat=Educat, Profes=Profes, like=like, Experience=Experience,
                                  Qualit=Qualit, Languag=Languag, Сomplang=Сomplang, Info=Info, Works=Works,
                                  Contacts=Contacts))
            await session.commit()


async def OnePhase(tg_id: BigInteger, FIO):
    async with async_session() as session:
        user = await session.scalar(select(User_name).where(User_name.tg_id == tg_id))

        if user is not User_name:
            session.add(User_name(FIO=FIO, tg_id=tg_id))
            await session.commit()


async def viev_all():
    async with async_session() as session:
        return await session.scalars(select(User_name))


async def get_ank(id_ank):
    async with async_session() as session:
        return await session.scalar(select(User_Info).where(User_Info.iad == id_ank))


async def Find_by_FIO(FIO):
    async with async_session() as session:
        return await session.scalar(select(User_Info).filter(User_Info.FIO.like(f'{FIO}%')))


async def Find_by_id():
    async with async_session() as session:
        return await session.scalars(select(User_Info).order_by(desc(User_Info.iad)).limit(2))


async def Find_by_prof(prof):
    async with async_session() as session:
        return await session.scalars(select(User_Info).filter(User_Info.Profes.like(f'%{prof}%')))


async def Find_by_lang(lang):
    async with async_session() as session:
        return await session.scalars(select(User_Info).filter(User_Info.Languag.like(f'%{lang}%')))


async def Find_by_qual(qual):
    async with async_session() as session:
        return await session.scalars(select(User_Info).filter(User_Info.Qualit.like(f'%{qual}%')))
