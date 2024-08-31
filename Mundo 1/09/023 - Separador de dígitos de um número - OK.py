# 023. Programa que leia um número de 0 a 9999 e mostre os digitos separados (unidade, dezena, centena, milhar).

numero23 = str(input('Digite um número de 0 a 9999: '))
numero23 = '000' + numero23
numero23.split()
print(str('{} milhares'.format(numero23[3])))
print(str('{} centenas'.format(numero23[2])))
print(str('{} dezenas'.format(numero23[1])))
print(str('{} unidades'.format(numero23[0])))