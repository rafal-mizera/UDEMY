import functools, time


def fib(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result


start = time.time()

for i in range(1,30):
    print(i,": ",fib(i))

stop = time.time()
print("Wykonanie funkcji zajęło:",stop-start)
print("-"*50)

start = time.time()

