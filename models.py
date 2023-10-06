from sqlalchemy import ForeignKey, Column, String, Integer, CHAR, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, DeclarativeBase, Mapped, mapped_column
from typing import List

# $ python create_tables.py


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    day_types: Mapped[List["DayTypes"]] = relationship(back_populates='user')

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return f"(UserID: {self.id} Username: {self.username})"


class DayTypes(Base):
    __tablename__ = "dayTypes"

    id: Mapped[int] = mapped_column(primary_key=True)
    day_type: Mapped[str] = mapped_column(nullable=False)
    date: Mapped[str] = mapped_column(nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped["Users"] = relationship(back_populates='dayTypes')
    exercises: Mapped[List["Exercises"]] = relationship(back_populates='day_types')

    def __repr__(self):
        return f"(DaytypeID: {self.id} DayType: {self.day_type} Date: {self.date})"


class Exercises(Base):
    __tablename__ = "exercises"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(nullable=False)
    weight: Mapped[int] = mapped_column(nullable=True)
    comment: Mapped[str] = mapped_column(nullable=True)
    day_types: Mapped["DayTypes"] = relationship(back_populates='exercises')

    day_type_id: Mapped[int] = mapped_column(ForeignKey('dayTypes.id'))

    def __repr__(self):
        return f"(ExerciseID: {self.id} Name: {self.name} Weight: {self.weight} Comment: {self.comment})"