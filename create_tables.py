from models import Base, Users, DayTypes, Exercises
from connect import engine

print("CREATING TABLES >>>> ")
Base.metadata.create_all(bind=engine)