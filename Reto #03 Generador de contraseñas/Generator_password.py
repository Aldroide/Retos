import random


def generator(length=8, capital=False, numbers=False, symbols=False):
    letters_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                    "y", "z"]
    numbers_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols_list = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    allletter = []
    password = ""

    [allletter.append(str(c)) for c in letters_list]

    if capital:
        [allletter.append(str(c).capitalize()) for c in letters_list]

    if numbers:
        [allletter.append(str(c).capitalize()) for c in numbers_list]

    if symbols:
        [allletter.append(str(c).capitalize()) for c in symbols_list]

    password = ""
    final_length = 8 if length < 8 else 16 if length > 16 else length

    while len(password) < final_length:
        password += str(random.choice(allletter))
    return password


print("1: ", generator())
print("2: ", generator(length=16))
print("3: ", generator(length=1))
print("4: ", generator(length=22))
print("5: ", generator(length=12, capital=True))
print("6: ", generator(length=12, capital=True, numbers=True))
print("7: ", generator(length=12, capital=True, numbers=True, symbols=True))
print("8: ", generator(length=12, capital=True, symbols=True))
