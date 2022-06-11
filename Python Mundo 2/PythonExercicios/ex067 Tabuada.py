while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    if valor < 0:
        break
    for cont in range (1, 11):
        print(f'{valor} x {cont} = {valor*cont}')
print('TABUADA ENCERRADA!')



