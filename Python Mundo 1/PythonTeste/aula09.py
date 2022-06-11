frase = '  Curso em Video Python  '
# fatiamento de string
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
# métodos
print(frase.count('o'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.find('r'))
print(len(frase))
print(len(frase.strip())) #strip tira espaços indesejáveis
print(frase.replace('Python', 'Android'))
print(frase.split())

print('Curso' in frase)







