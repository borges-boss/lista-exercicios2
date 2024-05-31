def fat(number:int):
    f = number
    while number > 1:
        f = f * (number - 1)
        number = number -1
    return f


def calculate_s(n):
    s = 0
    for i in range(1, n + 1):
        s += 1 / fat(i)
    return s


print(calculate_s(4))