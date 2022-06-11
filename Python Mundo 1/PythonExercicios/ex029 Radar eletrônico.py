velocidade = int(input('Qual a velocidade do carro em km/h: '))
vel = velocidade - 80
if velocidade > 80:
    valor = 7.00 * vel
    print('VOCÊ FOI MULTADO! E excedeu {} km/h, o valor da multa será R$ {:.2f}'.format(vel, valor))
else:
    print('Dirija com segurança!')




