print ('Gerador de PA')
print (10 * '-=')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 0
while cont < 10:
    print (termo, ' ↣ ', end=' ')
    cont += 1
    termo += razao
print ('FIM')



