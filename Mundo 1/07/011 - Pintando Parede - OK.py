#011. Programa que leia altura e largura de parede, calcule sua área e quantas litros de tinta será 
# necessário para pintá-la (1 litro de tinta = 2m²).

l_d011 = float(input('Qual a largura da parede? '))
a_d011 = float(input('Qual a altura da parede? '))
s_d011 = float(l_d011 * a_d011)
litros_tinta_d011 =  float(s_d011 / 2)
print('Você vai precisar de {:.1f} litros de tinta.'.format(litros_tinta_d011))