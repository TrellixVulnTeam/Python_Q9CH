from datetime import date
ano = int(input('Ano de nascimento: '))
anoatual = date.today().year
if anoatual - ano == 18:
    print('Você deve se alistar imediatamente!')
elif (anoatual - ano) < 18:
    print('Você ainda irá se alistar em {} anos, em {}.'.format(18 - (anoatual - ano), anoatual + (18 - (anoatual - ano))))
else:
    print('Você já passou do prazo de alistamento, deveria ter se alistado em {}.'.format(anoatual - ((anoatual - ano) - 18)))
