product_names = ['Produto1', 'Produto2', 'Produto3', 'Produto4', 'Produto5']
productPrices = [45, 75, 105, 30, 120]

product_below_50 = sum(price < 50 for price in productPrices)
product_below_50_and_100 = [product_names[i] for i in range(5) if 50 <= productPrices[i] <= 100]
product_above_100 = [price for price in productPrices if price > 100]
average_price_above_100 = sum(product_above_100) / len(product_above_100) if product_above_100 else 0

print("\nQuantidade de produtos com preço abaixo de R$ 50,00:", product_below_50)
print("\nProdutos com preço entre R$ 50,00 e R$ 100,00:", product_below_50_and_100)
print("\nMédia dos preços dos produtos com preço acima de R$ 100,00: R$", average_price_above_100)