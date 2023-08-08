import datetime
from datetime import datetime


class DayType:
    day_type = ""               # Push Pull or Legs
                                # NEED TO ADD DAY TRACKER IN MAIN (I THINK)

    current_date = datetime.now()     # xx-xx-xxxx
    str_date = current_date.strftime("%m-%d-%Y")

    def __init__(self, day_type):
        self.day_type = day_type

    def change_type(self, day_type):
        self.day_type = type

    def change_date(self, str_date):
        self.str_date = str_date

    def get_day_type(self):
        return self.day_type

    def get_date(self):
        return self.str_date


