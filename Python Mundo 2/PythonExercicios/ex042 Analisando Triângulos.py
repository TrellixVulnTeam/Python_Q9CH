r1 = float(input('Informe a primeira reta: '))
r2 = float(input('Informe a segunda reta: '))
r3 = float(input('Informe a terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('As linha com comprimento de {}, {} e {} formam um triângulo EQUILÁTERO.'.format(r1, r2, r3))
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('As linha com comprimento de {}, {} e {} formam um triângulo ESCALENO.'.format(r1, r2, r3))
    else:
        print('As linha com comprimento de {}, {} e {} formam um triângulo ISÓSCELES.'.format(r1, r2, r3))
else:
    print('As linhas não formam um triângulo!')
