print('''Suas opções:
(0) PEDRA
(1) PAPEL
(2) TESOURA''')
jog = int(input('Qual é a sua jogada? '))
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2) #itens[comp]
from time import sleep
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print(12 * '-=')
print('Computador jogou {} '.format(itens[comp]))
print('Jogador jogou {} '.format(itens[jog]))
print(12 * '-=')
if comp == 0:
    if jog == 0:
        print('EMPATE!')
    elif jog == 1:
        print('JOGADOR VENCEU!')
    elif jog == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA.')
elif comp == 1:
    if jog == 0:
        print('COMPUTADOR VENCEU!')
    elif jog == 1:
        print('EMPATE!')
    elif jog == 2:
        print('JOGADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA.')
else:
    if jog == 0:
        print('JOGADOR VENCEU!')
    elif jog == 1:
        print('COMPUTADOR VENCEU!')
    elif jog == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA.')









