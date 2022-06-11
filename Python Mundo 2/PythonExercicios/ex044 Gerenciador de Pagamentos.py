preço = float(input('Valor da compra R$ '))
print('FORMAS DE PAGAMENTO:')
print('(1) à vista dinheiro/cheque: 10% de desconto.')
print('(2) à vista no cartão: 5% de desconto.')
print('(3) em até 2x no cartão: preço formal.')
print('(4) 3x ou mais no cartão: 20% de juros.')
opçao = int(input('Qual Opção: '))
if opçao == 1:
    avista = preço - (preço * 10/100)
    print('Com 10% de desconto será R$ {:.2f}'.format(avista))
elif opçao == 2:
    avistacartao = preço - (preço * 5/100)
    print('Com 5% de desconto será R$ {:.2f}'.format(avistacartao))
elif opçao == 3:
    print('O preço do produto é R$ {:.2f}'.format(preço))
elif opçao == 4:
    parcela = int(input('Quantas parcelas?'))
    cartao3x = preço + (preço * 20/100)
    mensal = cartao3x / parcela
    print('Parcelado em {} vezes, o juros é de 20%.'.format(parcela))
    print('O valor total é R$ {:.2f}, e mensal será R$ {:.2f}'.format(cartao3x, mensal))
else:
    print('Opção invalida. Tente novamente.')
    



