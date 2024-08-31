# Programa que leia o tamanho dos lados de um triângulo e diga se pode ser um triângulo ou não. Se sim, se vai ser equilátero, isósceles ou escaleno.

a = float(input('Digite o tamanho da reta A: '))
b = float(input('Digite o tamanho da reta B: '))
c = float(input('Digite o tamanho da reta C: '))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print('As retas podem formar um triângulo.')
    if a == b and a != c or a == c and a != b or b == c and b !=a:
        print('Seu triângulo é isósceles.')
    elif a == b == c:
        print('Seu triângulo é equilátero.')
    else:
        print('Seu triângulo é escaleno.')
else:
    print('As retas não podem formar um triângulo.')