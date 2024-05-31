
vector = [0]*6
evens = []
odds = []

for i in range(6):
    vector[i] = int(input("Digite um número inteiro: "))


for num in vector:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)


print("\nQuantidade de números pares: ", len(evens))
print("Números pares: ", evens)

print("\nQuantidade de números ímpares: ", len(odds))
print("Números ímpares: ", odds)