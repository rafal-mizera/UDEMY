numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

x = 1
max = len(numbers) - 2

while x < max:
    print(numbers[x],"and",numbers[x+1],"and",numbers[x+2])
    if numbers[x+1] == numbers[x]**2 and numbers[x+2] == numbers[x+1]**2:
        print("\tFOUND!!!")
    x +=1

print("{:10s}".format("xx"),"traa")