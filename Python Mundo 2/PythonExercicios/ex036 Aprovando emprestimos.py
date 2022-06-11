casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual seu salário? '))
anos = int(input('Quantos anos para pagar? '))
mensal = casa / (anos * 12)
if mensal <= (salario * 30/100):
    print('O valor da casa é R$ {:.2f}, parcelado em {} anos, no valor de R$ {:.2f}. Com seu salário de R$ {:.2f} foi CONCEDIDO o empréstimo.'.format(casa, anos, mensal, salario))
else:
    print('O valor da casa é R$ {:.2f}, parcelado em {} anos, no valor de R$ {:.2f}. Com seu salário de R$ {:.2f} foi RECUSADO o empréstimo.'.format(casa, anos, mensal, salario))

