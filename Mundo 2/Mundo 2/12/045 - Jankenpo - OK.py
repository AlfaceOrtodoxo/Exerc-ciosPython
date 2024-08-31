# Crie um programa que jogue jokenpô com você.

import random

print("Bem-vindo ao Jankenpo!")
print("Escolha uma opção:")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")

escolhajogador = int(input('Qual você escolhe? ')) - 1

opcoes = ['Pedra', 'Papel', 'Tesoura']

escolhapc = random.randint(0,2)

print(f'Você escolheu: {opcoes[escolhajogador]}')
print(f'O Computador escolheu: {opcoes[escolhapc]}')

if escolhapc == escolhajogador:
    print('Deu empate.')
elif (escolhapc == 0 and escolhajogador == 1) or (escolhapc == 1 and escolhajogador == 2) or (escolhapc == 2 and escolhajogador == 0):
    print('O jogador venceu.')
else:
    print('O jogador perdeu.')

