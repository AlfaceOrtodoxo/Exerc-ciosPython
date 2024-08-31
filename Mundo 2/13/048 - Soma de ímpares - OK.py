# Programa que some todos os numeros ímpares multiplos de 1 e 3 e que se encontram no intervalo de 1 até 500.

s = 0
for c in range(3, 501, 3):
    s += c
print(s)