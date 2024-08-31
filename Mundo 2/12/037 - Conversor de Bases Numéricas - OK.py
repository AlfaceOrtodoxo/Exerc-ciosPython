#Escreva um programa que escreva um numero inteiro qualquer e peça para o usuário escolher qual será a base de conversão.
#1 para binário, 2 para octal e 3 para hexadecimal

num = int(input('Digite um número inteiro: '))
escolha = int(input('Digite 1 para converter o número para binário, 2 para octal e 3 para hexadecimal: '))
if escolha == 1:
    num = bin(num)
    print(f'Seu número em binário é: {num}.')
elif escolha == 2:
    num = oct(num)
    print(f'Seu número em octal é: {num}.')
elif escolha == 3:
    num = hex(num)
    print(f'Seu número em hexadecimal é: {num}.')