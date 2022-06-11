from datetime import date
maior = 0
menor = 0
anoatual = date.today().year
for c in range(1, 8):
    ano = int(input('Em que ano nasceu a {}ª pessoa? '.format(c)))
    if anoatual - ano >= 18:
        maior += 1
    else:
        menor += 1
print('Tem {} pessoas maiores de idade.'.format(maior))
print('Tem {} pessoas menores de idade. '.format(menor))


