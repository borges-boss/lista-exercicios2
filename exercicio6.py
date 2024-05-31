number = -1


def sum_all(number):
    return sum(i for i in range(number + 1))


while number <= -1:
    number = int(input("Por favor digite um numero inteiro positivo: "))
    if number > -1:
     print(sum_all(number))