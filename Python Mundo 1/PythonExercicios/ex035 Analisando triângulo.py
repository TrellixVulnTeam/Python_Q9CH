reta1 = float(input('Informe a primeira reta: '))
reta2 = float(input('Informe a segunda reta: '))
reta3 = float(input('Informe a terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('As linha com comprimento de {}, {} e {} formam um triângulo'.format(reta1, reta2, reta3))
else:
    print('As linhas não formam um triângulo!')
