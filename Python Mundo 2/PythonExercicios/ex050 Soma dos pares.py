soma = 0
for c in range(1, 7):
    num = int(input('Informe o número {}: '.format(c)))
    if num % 2 == 0:
        soma += num
print('A soma dos pares é {} '.format(soma))

