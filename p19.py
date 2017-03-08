import datetime
total = 0
for date in (datetime.datetime(1901, 1, 1) +
             datetime.timedelta(n) for n in range(36525)):
    print(date, date.weekday(), date.day)
    total += (date.weekday() == 6) and (date.day == 1)

print(total)
