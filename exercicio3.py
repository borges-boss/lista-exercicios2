sales = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
commissions = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
names = ['Ana', 'Beto', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda', 'Gustavo', 'Helena', 'Igor', 'Julia']
values_to_receive = [0]*10


for i in range(10):
    values_to_receive[i] = sales[i] * (commissions[i]/100)


total_sales = sum(sales)
maior_valor = max(values_to_receive)
menor_valor = min(values_to_receive)
vendedor_maior_valor = names[values_to_receive.index(maior_valor)]
vendedor_menor_valor = names[values_to_receive.index(menor_valor)]


print("\nRelatório:")
for i in range(10):
    print(names[i], "irá receber R$", values_to_receive[i])

print("\nTotal das vendas de todos os vendedores: R$", total_sales)
print("\nMaior valor a receber: R$", maior_valor, "- Vendedor:", vendedor_maior_valor)
print("\nMenor valor a receber: R$", menor_valor, "- Vendedor:", vendedor_menor_valor)