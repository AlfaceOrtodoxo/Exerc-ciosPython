#Crie um programa que leia varios numeros e adicione-os em uma lista. No final deve mostrar:
#Quantos valores foram digitados, lista decrescente e se o valor 5 foi digitado e está ou não na lista.

lista = []
c = 0

while True:
    lista.append(int(input('Digite um número: ')))
    c += 1
    cont = str(input('Quer continuar? [S/N]: ')).upper()
    if cont in 'N':
        break


print(f'Foram digitados {c} valores na lista.')
if 5 in lista:
    print(f'O número 5 está na lista, na posição {lista.index(5)}')
else:
    print('O número 5 não está na lista.')

lista.sort()
lista.reverse()

print(f'A lista reversa é {lista}.')