#Crie um programa que leia varios numeros e adicione-os em uma lista. No final deve mostrar:
#Duas listas extras dividindo os valores pares e impares em ordem de input. Usar dois loops.

lista = []
pares = []
impares = []
cont = ''

while True:
    lista.append(int(input('Digite um número: ')))
    cont = str(input('Quer continuar? [S/N]: ')).upper()
    if cont in 'N':
        break

for v in lista:
    if v % 2 == 0:
        pares.append(v)
    if v % 2 != 0:
        impares.append(v)

print(f'A lista completa é {lista}.')
print(f'Os pares são {pares}.')
print(f'Os ímpares são {impares}.')
