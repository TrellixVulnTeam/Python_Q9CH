from datetime import date
anonasc = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - anonasc
print('Você tem {} anos. '.format(idade))
if idade <= 9:
    print('Classificação: MIRIM.')
elif 9 < idade <= 14:
    print('Classificação: INFANTIL.')
elif 14 < idade <= 19:
    print('Classificação: JÚNIOR.')
elif 19 < idade <= 25:
    print('Classificação: SÊNIOR.')
else:
    print('Classificação: MASTER.')
    



