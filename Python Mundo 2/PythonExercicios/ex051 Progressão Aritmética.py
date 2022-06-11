print(19 * '=')
print('10 TERMOS DE UMA PA')
print(19 * '=')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range(1, 11):
    print(termo, ' ↣ ', end=' ')
    termo += razao
print('Acabou!')