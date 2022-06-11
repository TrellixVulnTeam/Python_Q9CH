print(30 * '{}-={}'.format('\033[31m', '\033[m'))
print('{}Vou pensar em um número entre 0 e 10, tente acertar qual é...{} '.format('\033[30;41m', '\033[m'))
print(30 * '{}-={}'.format('\033[31m', '\033[m'))
from random import randint
comp = randint(0, 10)
jog = int(input('Qual seu palpite? '))
tentativas = 0
while jog != comp:
    if jog > comp:
        jog = int(input('Menos... Tente novamente: '))
    else:
        jog = int(input('Mais... Tente novamente: '))
    tentativas += 1
print('Acertou com {} tentativas. Parabéns!!!'.format(tentativas))









