import random
v = 0
while True:
    print(15 * '=-')
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print(15 * '=-')
    computador = random.randint(0, 10)
    jogador = int(input('Diga um valor: '))
    soma = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
            tipo = str(input('Par ou Ímpar [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador},e o computador jogor {computador}. Total de {soma}.')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if soma % 2 != 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER. Você venceu {v} vezes.')

















