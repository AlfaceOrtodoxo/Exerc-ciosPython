#O Computador vai pensar em um numero de 1 a 10 e o jogador só vai parar de tentar advinhar quando acertar.

import random

numpc = random.randint(1,10)

#print(numpc)

numjog = int(input('Tente advinhar o número, de 1 a 10: '))
numpal = 1

while numjog != numpc:
    numjog = int(input('Número errado, tente novamente: '))
    numpal += 1
print(f'Parabéns, você acertou, e levou só {numpal} palpites!')
