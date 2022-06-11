nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome com letras maiúsculas ', nome.upper())
print('Seu nome com letras minúsculas ', nome.lower())
print('Seu nome tem {} letras '.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras '.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome tem {} letras '.format(len(separa[0])))







