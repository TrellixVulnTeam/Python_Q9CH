num = int(input('Informe um número para a conversão: '))
print('Digite 1 para BINÁRIO')
print('Digite 2 para OCTAL')
print('Digite 3 para HEXADECIMAL')
base = int(input('Escolha a base numérica: '))
if base == 1:
    print('{} em BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} em OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} em HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('valor inválido!')


