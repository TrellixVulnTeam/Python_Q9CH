l = float(input('Informe a largura da parede: '))
a = float(input('Informe a altura da parede: '))
area = l*a
print('A área total da parede é {}m2.'.format(area))
print('Para {}m2 é necessário {} litros de tinta. '.format(area, (area/2)))
