primeirovalor = int(input('Primeiro Valor: '))
segundovalor = int(input('Segundo Valor: '))
opcao = 0
while opcao != 5:
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        resultado = primeirovalor + segundovalor
        print('{} + {} = {}'.format(primeirovalor, segundovalor, resultado))
    elif opcao == 2:
        resultado = primeirovalor * segundovalor
        print('{} x {} = {}'.format(primeirovalor, segundovalor, resultado))
    elif opcao == 3:
        if primeirovalor > segundovalor:
            print('{} é maior que {}'.format(primeirovalor, segundovalor))
        else:
            print('{} é maior que {}'.format(segundovalor, primeirovalor))
    elif opcao == 4:
        print('Informe os números novamente')
        primeirovalor = int(input('Primeiro Valor: '))
        segundovalor = int(input('Segundo Valor: '))
    elif opcao == 5:
        print('Programa finalizado!')
    else:
        print('Opção inválida, tente novamente:')




