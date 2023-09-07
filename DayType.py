import datetime
from datetime import datetime


class DayType:
    day_type = ""               # Push Pull or Legs
    current_date = datetime.now()     # xx-xx-xxxx
    str_date = current_date.strftime("%m-%d-%Y")

    def __init__(self, day_type):
        if day_type == "push":
            # Creates exercise dictionaries
            self.push_exercises = {}
            self.day_type = day_type

        elif day_type == "pull":
            self.pull_exercises = {}
            self.day_type = day_type

        elif day_type == "legs":
            self.leg_exercises = {}
            self.day_type = day_type

    def change_type(self, day_type):
        self.day_type = day_type

    def change_date(self, str_date):
        self.str_date = str_date

    def get_day_type(self):
        return self.day_type

    def get_date(self):
        return self.str_date

    def get_push_exercises(self):
        return self.push_exercises

    def get_pull_exercises(self):
        return self.pull_exercises

    def get_legs_exercises(self):
        return self.leg_exercises
