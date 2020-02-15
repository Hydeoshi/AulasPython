import calendar
print(calendar.weekheader(3))
print()
print(calendar.firstweekday())
print()
print(calendar.month(2020, 2, w=3))
print()
print(calendar.monthcalendar(2020, 2))
print()
print(calendar.calendar(2020, w=3))

for c in range(1, 13):
    print(calendar.monthcalendar(2020, c))

day_of_the_week = calendar.weekday(2020, 1, 31)

print(day_of_the_week)

is_leap = calendar.isleap(2020)
print(is_leap)

how_many_leap_years = calendar.leapdays(2000, 2021)
print(how_many_leap_years)