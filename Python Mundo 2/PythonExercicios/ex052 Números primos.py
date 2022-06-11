n = int(input('Digite um número: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        cont += 1
        print('\033[31m', end=' ')
    else:
        print('\033[m', end=' ')
    print(c, end='')
print('\033[m\nO número {} foi divisível por {} vezes.'.format(n, cont))
if cont == 2:
    print('O número {} é primo.'.format(n))
else:
    print('O número {} não é primo.'.format(n))






