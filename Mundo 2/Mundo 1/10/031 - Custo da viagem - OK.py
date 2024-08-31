#032 Escreva um programa que leia a distancia de uma viagem em KM e calcule o preço da passagem. 50 centavos para viagens de até 200 km e 45 centavos para viagens de mais de 200 km.


dist031 = float(input('Quantos km daqui pra lá? '))
if dist031 <= 200.00:
    valorme200 = dist031 * 0.5
    print('A passagem vai custar {:.2f}.'.format(valorme200))
else:
    valorma200 = dist031 * 0.45
    print('A passagem vai custar {:.2f}.'.format(valorma200))
print('-----FIM-----')