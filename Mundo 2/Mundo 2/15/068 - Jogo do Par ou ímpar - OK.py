# Programa para jogar par ou ímpar com o computador. O programa só será interrompido quando o jogador perder. Colocar contador de vitória que será mostrado no final.

import random

numpc = 0
numjog = 0
perdeu = False
escjog = ''

while True:
    print('------ PAR OU ÍMPAR ------')
    print('------ O JOGO PARA QUANDO VOCÊ PERDER ------')
    numjog = int(input('Escolha um número: '))
    escjog = str(input('Ímpar ou Par? [I/P]: ')).upper()
    numpc = random.randint(1,6)
    if (numjog + numpc) % 2 == 0 and escjog in 'P':
        print(f'O resultado é {numjog + numpc}, então você ganhou!')
    elif (numjog + numpc) % 2 != 0 and escjog in 'I':
         print(f'O resultado é {numjog + numpc}, então você ganhou!')
    elif (numjog + numpc) % 2 == 0 and escjog in 'I':
        break
    elif (numjog + numpc) % 2 != 0 and escjog in 'P':
        break
print(f'O resultado é {numjog + numpc}, então você perdeu.')

