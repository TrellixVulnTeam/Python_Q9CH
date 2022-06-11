nome = str(input('Qual é seu nome: ')).upper()
if nome == 'WELLINGTON':
    print('Que nome bonito!')
elif nome == 'MARIA' or nome == 'JOÃO' or nome == 'PAULO' or nome == 'PEDRO':
    print('Seu nome é bem popular')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))



