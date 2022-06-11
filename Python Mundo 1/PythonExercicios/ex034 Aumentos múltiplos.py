salario = float(input('\033[4;35;40mQual seu salário? R$\033[m '))
print('Para salários acima de R$ 1250,00 o aumento é de 10%, e abaixo é de 15%.')
if salario <= 1250:
    print('Seu salário terá um aumento de 15%. Você irá receber R$ {:.2f}'.format(salario + (salario * 15 / 100)))
else:
    print('Seu salário terá um aumento de 10%. Você irá receber R$ {:.2f}'.format(salario + (salario * 10 / 100)))

