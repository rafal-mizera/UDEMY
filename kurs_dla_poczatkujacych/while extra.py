initialCapital = 20000
percent = 0.03
maxTimeYears = 10
time = 0
capital = initialCapital

while time <= maxTimeYears:
    capital += capital * percent
    print(capital)
    time += 1
####################################
num = 20730906
num = str(num)
sum = 0

for d in num:
    sum += int(d)

print(sum)


