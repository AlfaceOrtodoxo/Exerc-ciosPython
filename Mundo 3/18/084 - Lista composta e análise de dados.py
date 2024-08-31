# Faça um programa que leia o nome e peso de várias pessoas guardando em uma lista. No final, mostre:
# Quantas pessoas foram cadastradas, uma listagem das pessoas mais pesadas e uma listagem das mais leves.

lista1 = ['',0]
lista2 = list()

pesos = [0.0]




while True:
    nome = str(input("Nome: "))
    peso = float(input("Peso: "))
    lista1 [0] = nome
    lista1 [1] = peso
    #pesos [0] = peso
    pesos.append(peso)
    lista2.append(lista1[:])
    cont = str(input('Continuar? [S/N]: ')).lower()
    if cont != 's':
        break

print(lista2)
print(peso)