import datetime

month_n_days = {1: 31, 2: 28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def num_days_in_month(y:int, m:int):
    """ given the year and month, return number of days in a month """
    if m == 2: # february
        if y % 100 == 0: # end of century
            if y % 400 == 0: return 29 # Leap century year
            else: return 28
        elif y % 4 == 0: return 29 # Leap, non-century year
        else: return 28
    else: # Not February
        return month_n_days[m]

def first_day_next_month(dt : datetime.date) -> datetime.date:
    last_day_of_month = datetime.date(dt.year, dt.month, num_days_in_month(dt.year, dt.month))
    return last_day_of_month + datetime.timedelta(days = 1)

start_date = datetime.date(year = 1901, month = 1, day = 1)
end_date = datetime.date(year = 2000, month = 12, day = 31)

desired_weekday = 7 # isoweekday for sunday
d = start_date
n_sundays = 0
while d <= end_date:
    if d.isoweekday() == desired_weekday:
        n_sundays += 1
    d = first_day_next_month(d)