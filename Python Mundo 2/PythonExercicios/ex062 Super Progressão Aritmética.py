print('Gerador de PA')
print(10 * '-=')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
total = 0
qtde = 10
while qtde != 0:
    total += qtde
    while cont <= total:
        print('{} ↣'.format(termo), end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    qtde = int(input('Quantos termos você quer mostrar a mais: '))
print('FIM')




