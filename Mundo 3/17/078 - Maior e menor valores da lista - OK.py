#Programa que leia 5 valores numéricos e os armazene em uma lista. No final mostre o maior e o menor valor e suas posições na lista.

valor = []

for c in range(0,5):
    valor.append(int(input('Digite um número: ')))



valoremordem = sorted(valor[:])
maior = valoremordem[4]
menor = valoremordem[0]



print(f'O maior valor foi {maior} que aparece na posição {valor.index(maior)} e o menor valor foi {menor} que aparece na posição {valor.index(menor)}.')
