import functools,time

def wrapperTime(func):
    def Wrapper(*args,**kwargs):
        time_start = time.time()
        v = func(*args,*kwargs)
        time_stop = time.time()
        print(f"Funkcja <{func.__name__}> wykonana w czasie {time_stop - time_start}")
        return v
    return  Wrapper



@wrapperTime
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v


print(get_sequence(5))


#######################################################################
def nice_to_meet_you(func):
    def Wrapper(*args,**kwargs):
        f = func(*args,*kwargs)
        print("Nice to meet You!!!")
        return f
    return Wrapper


@nice_to_meet_you
def hello(*names):
    for name in names:
        print("Hello",name)





print(hello("Rafał","Aga"))







