# 022. Programa que leia e mostre o nome completo da pessoa todo maiúsculo, 
# todo minúsculo, quantidade de letras sem contar espaços e quantas letras tem o primeiro nome.

nome22 = input('Qual o teu nome? ')
print(nome22.upper())
print(nome22.lower())
nome22 = nome22.replace(' ', '')
print(len(nome22))
nome22 = nome22.split()
print(len(nome22[0]))