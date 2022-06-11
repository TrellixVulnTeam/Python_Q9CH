nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Com notas {} e {}, sua média é {}, e está'.format(nota1, nota2, media))
if media < 5:
    print('REPROVADO')
elif media >= 5 and media <= 6.9:
    print('em RECUPERAÇÃO')
else:
    print('APROVADO')
