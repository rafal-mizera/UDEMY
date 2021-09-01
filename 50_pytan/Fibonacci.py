def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

def fibonacci_l(n):
    p,d = 0,1
    for _ in range(n):
        p,d = d,p+d
    return p

print(fibonacci_l(10))