# Programa que leia um número qualquer que leia um número e mostre o seu fatorial.

n1 = int(input('Digite um número: '))
nprod = n1 - 1

while nprod != 1:
    n1 = n1 * nprod
    nprod -= 1
print (f'O fatorial é {n1}.')