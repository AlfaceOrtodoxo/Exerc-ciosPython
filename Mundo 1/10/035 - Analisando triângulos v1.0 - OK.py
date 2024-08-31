#035 Escreva um programa que leia o comprimento de tres retas e diga se elas podem ou não formar um triângulo.


n1035 = float(input('Digite um número: '))
n2035 = float(input('Digite outro número: '))
n3035 = float(input('Digite mais um número: '))
if (n1035 + n2035) > n3035 and (n2035 + n3035) > n1035 and (n1035 + n3035) > n2035:
    print('Essas medidas podem formar um triângulo.')
else:
    print('Essas medidas não podem formar um triângulo.')
