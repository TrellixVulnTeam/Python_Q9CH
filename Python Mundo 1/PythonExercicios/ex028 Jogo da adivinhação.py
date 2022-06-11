print(30 * '{}-={}'.format('\033[31m', '\033[m'))
print('{}Vou pensar em um número entre 0 e 5, tente acertar qual é...{} '.format('\033[30;41m', '\033[m'))
print(30 * '{}-={}'.format('\033[31m', '\033[m'))
import random
from time import sleep # módulo para tempo de espera
num = [0, 1, 2, 3, 4, 5]
comp = random.choice(num)
jog = int(input('Em que número eu pensei? '))
print('\033[33mPROCESSANDO...\033[m')
sleep(2)
if comp == jog:
    print('PARABÉNS VOCÊ ACERTOU!')
else:
    print('GANHEI! pensei no número {} e não no número {}.'.format(comp, jog))
    






