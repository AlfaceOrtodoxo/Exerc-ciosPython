#Crie um programa que leia uma frase e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().lower().replace(' ', '')  
n = len(frase)
inv = ''

for c in range (n-1, -1, -1):
    inv += frase[c]
print (inv)

if inv == frase:
    print('A sua frase é um palíndromo.')
else:
    print('A sua frase não é um palíndromo.') 
    

