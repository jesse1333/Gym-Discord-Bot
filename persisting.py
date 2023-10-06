from models import Users, DayTypes, Exercises
from sqlalchemy.orm import Session
from connect import engine

session = Session(bind=engine)

user = Users("Jesse")
session.add(user)                             # this creates the person in the database
session.commit()

