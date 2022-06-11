sublinhado = '\033[4m'
fechamento = '\033[m'
distancia = float(input('Qual a distância da sua viagem em {}km{}? '.format(sublinhado, fechamento)))
if distancia <= 200:
    print('O preço da passagem é R$ {:.2f}'.format(distancia * 0.50))
else:
    print('O preço da passagem é R$ {:.2f}'.format(distancia * 0.45))

