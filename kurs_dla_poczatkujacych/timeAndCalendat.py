import time

print(time.time())
print(time.localtime(time.time()))

import calendar

calendar.setfirstweekday(6)
print(calendar.month(1992,11))

print(calendar.isleap(2000))

print(calendar.calendar(2019))