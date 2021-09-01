numbers = [10,2,4,120,1000,7,-12]

print(max(numbers) - min(numbers))

print(sorted(numbers)[-1] - sorted(numbers)[0])

min = numbers[0]
max = numbers[0]
for x in numbers:
    if x < min:
        min = x
    elif x > max:
        max = x
print(max - min)