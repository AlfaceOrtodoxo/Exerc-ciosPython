#032 Escreva um programa que leia um ano e diga se ele é bissexto ou não.



ano032 = int(input('Digite um ano: '))
if ano032 % 4 == 0:
    print('O ano é bissexto.')
else:
    print('O ano não é bissexto.')