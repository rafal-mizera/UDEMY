def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

a_str = input("Podaj współcznnik a: ")
b_str = input("Podaj współcznnik b: ")
c_str = input("Podaj współcznnik c: ")

if not (check_int(a_str) and check_int(b_str) and check_int(c_str)):
    print("a, b and c need to be int!")
else:
    a = int(a_str)
    b = int(b_str)
    c = int(c_str)
    if a == 0:
        print("To nie jest równanie kwadratowe!!!")
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            print("Brak rozwiązań dla podanych danych!!!")
        elif delta == 0:
            x1 = (-1 * b - pow(delta,0.5)) / 2*a
            print(f"Rozwiązaniem równania jest liczba: {x1}")

        elif delta > 0:
            x1 = (-1 * b - pow(delta, 0.5)) / 2 * a
            x2 = (-1 * b + pow(delta, 0.5)) / 2 * a
            print(f"Rozwiązaniem równania są liczby: {x1} oraz {x2}")





