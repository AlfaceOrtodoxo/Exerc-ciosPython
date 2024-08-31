# Crie um programa que cria 5 numeros aleatorios e guarde numa tupla. Depois, mostre a listagem de números e indique o menor e o maior valor da tupla.

import random

aleatorio = random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10)
sortedaleat = sorted(aleatorio)

print(sortedaleat)
print(f'O menor número é {sortedaleat[0]}.')
print(f'O maior número é {sortedaleat[4]}.')