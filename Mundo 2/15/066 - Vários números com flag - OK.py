# Programa que leia vários números inteiros. Flag de parada 999. Ao final mostre quantos números leu e a soma entre eles.

n = s = c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    c += 1
print (f'A soma vale {s} e foram lidos {c} termos.')