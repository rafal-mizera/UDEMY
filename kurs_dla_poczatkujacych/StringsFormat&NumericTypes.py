name = "Rafał"
age = 27
daysInYear = 365
message = '%s is %d years old, so is about %d days old'
print(message % (name,age,daysInYear*age))
print(message % ("Jan",26,26*daysInYear))
message = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format("Chris",17,17*daysInYear))

division = 1234567890 // 12345
rest = 1234567890 % 12345

print(f"1234567890 divided by 12345 is {division} and the rest is {rest}")