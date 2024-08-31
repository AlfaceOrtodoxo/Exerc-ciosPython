#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
div = 0

for c in range (1,n+1):
    if n % c == 0:
        div += 1

if div > 2:
    print ('O número foi divisível por mais de duas vezes, portanto não é primo.')
else:
    print ('O número só foi divisível duas vezes portanto é primo.')


        
    