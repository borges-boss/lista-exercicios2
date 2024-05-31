def fat(number:int):
    f = number
    while number > 1:
        f = f * (number - 1)
        number = number -1
    return f



print(fat(7))
    



