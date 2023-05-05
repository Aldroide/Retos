import random


def generator(length=8, capital=False, numbers=False, symbols=False):

    # fuente https://www.ascii-code.com

    caracter = list(range(97, 123))

    if symbols:
        caracter += list(range(33, 48)) +\
            list(range(58, 65))+list(range(91, 97))

    if numbers:
        caracter += list(range(48, 58))

    if capital:
        caracter += list(range(65, 91))
    password = ""
    final_length = 8 if length < 8 else 16 if length > 16 else length

    while len(password) < final_length:
        password += chr(random.choice(caracter))

    return password


print(generator())
print(generator(length=16))
print(generator(length=1))
print(generator(length=22))
print(generator(length=12, capital=True))
print(generator(length=12, capital=True, numbers=True))
print(generator(length=12, capital=True, numbers=True, symbols=True))
print(generator(length=12, capital=True, symbols=True))
