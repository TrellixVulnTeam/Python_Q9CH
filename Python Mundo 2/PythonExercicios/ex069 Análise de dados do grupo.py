maior_idade = 0
homens = 0
mulheres_menor20 = 0
while True:
    print(10 * '--')
    print('CADASTRE UMA PESSOA')
    print(10 * '--')
    idade = int(input('Idade: '))
    if idade >= 18:
        maior_idade += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menor20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total de pessoas com mais de 18 anos é {maior_idade}.')
print(f'Foram cadastrados {homens} homens.')
print(f'E tem {mulheres_menor20} mulheres com menos de 20 anos.')








