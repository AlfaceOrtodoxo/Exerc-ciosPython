# Refaça o desafio 51 que dessa vez mostra os 10 primeiros termos da PA usando while.

n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

termos = 0

print (n1)
while termos < 9:
    termos += 1
    n1 += r
    print (n1)