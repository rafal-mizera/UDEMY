def stars(func):
    def decorated_with_stars():
        print("***")
        func()
        print("***")
    return decorated_with_stars

@stars
def myFunction():
    print("bla bla bla")


myFunction()