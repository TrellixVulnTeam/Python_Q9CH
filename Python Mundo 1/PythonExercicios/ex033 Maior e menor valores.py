num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
# menor valor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num2 and num3 < num1:
    menor = num3
# maior valor
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))



