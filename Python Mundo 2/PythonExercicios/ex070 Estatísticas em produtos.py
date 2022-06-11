totalGasto = mais1000 = menor = cont = 0
barato = ' '
while True:
    nome = str(input('Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    totalGasto += preco
    if preco > 1000:
        mais1000 += 1
    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total gasto foi R$ {totalGasto:.2f}')
print(f'Tem {mais1000} produtos que custam mais de R$ 1000,00')
print(f'O produto mais barato é {barato} e custa R$ {menor:.2f}')






