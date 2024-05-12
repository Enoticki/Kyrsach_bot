from sqlalchemy import BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User_name(Base):
    __tablename__ = 'Name'
    iad: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    FIO: Mapped[str] = mapped_column()
    tg_id = mapped_column(BigInteger)


class User_Info(Base):
    __tablename__ = 'Users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    FIO: Mapped[str] = mapped_column()
    Educat: Mapped[str] = mapped_column()
    Profes: Mapped[str] = mapped_column()
    like: Mapped[str] = mapped_column()
    Experience: Mapped[str] = mapped_column()
    Qualit: Mapped[str] = mapped_column()
    Languag: Mapped[str] = mapped_column()
    Info: Mapped[str] = mapped_column()
    Works: Mapped[str] = mapped_column()
    Contacts: Mapped[str] = mapped_column()


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
