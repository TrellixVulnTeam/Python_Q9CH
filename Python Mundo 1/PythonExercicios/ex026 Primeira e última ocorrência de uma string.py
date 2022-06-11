frase = str(input('Digite uma frase: ')).strip()
a1 = frase.lower().find('a')
aq = frase.lower().count('a')
au = frase.lower().rfind('a')
print('A letra A aparece {} vezes '.format(aq))
print('A primeira letra A aparece na posição {} '.format(a1 + 1))
print('A última letras A aparece na posição {} '.format(au + 1))




