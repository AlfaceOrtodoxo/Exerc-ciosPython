# 016. Crie um programa que leia qualquer número real e mostre sua parte inteira.
# Pacote utilizado: math

from math import trunc
num_d016 = float(input('Digite um número com pelo menos uma casa decimal: '))
num_int_d016 = trunc(num_d016)
print('A parte inteira do número {} é {}.'.format(num_d016, num_int_d016))