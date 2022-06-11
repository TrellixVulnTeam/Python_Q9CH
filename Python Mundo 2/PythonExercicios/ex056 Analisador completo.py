somaidade = 0
velho = 0
nomevelho = ''
mulher = 0
for p in range(1, 5):
    print('{} {}ª PESSOA {}'.format(5 * '-', p, 5 * '-'))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade += idade
    mediaidade = somaidade / 4
    if sexo == 'M':
        if p == 1:
            velho = idade
            nomevelho = nome
        else:
            if idade > velho:
                velho = idade
                nomevelho = nome
    if sexo == 'F' and idade < 20:
        mulher += 1
print('A média de idade do grupo é {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(velho, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulher))



