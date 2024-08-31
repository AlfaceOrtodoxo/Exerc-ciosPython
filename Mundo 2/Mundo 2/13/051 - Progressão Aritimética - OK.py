#Programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos da progressão.

p1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

for c in range(0,10):
    p1 += r
    print(p1)