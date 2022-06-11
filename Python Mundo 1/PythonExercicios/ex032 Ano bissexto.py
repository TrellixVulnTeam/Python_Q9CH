from datetime import date
ano = int(input('Digite o ano ou 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year # para pegar ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é \033[7mBISSEXTO\033[m'.format(ano))
else:
    print('O ano {} não é \033[7mBISSEXTO\033[m'.format(ano))

