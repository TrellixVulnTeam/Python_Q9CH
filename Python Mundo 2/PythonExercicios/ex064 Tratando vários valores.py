num = 0
soma = 0
qtdenum = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    qtdenum += 1
    soma += num
print('Você digitou {} números e a soma é {}.'.format(qtdenum-1, soma-999))





