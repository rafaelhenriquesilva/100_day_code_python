import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
print(day_of_week)
print(month)

date_of_birth = dt.datetime(year=1997, month=2, day=28)
print(date_of_birth)