#028 Faça o computador pensar em um número entre 0 e 5, e um input para que o usuário tente advinhar esse número.

import random
sorteado28 = random.randint(0, 5)
guess28 = int(input('Digite um número de 0 a 5: '))
if sorteado28 == guess28:
    print('Parabéns, você advinhou certo!')
else:
    print('O computador ganhou, vish!')