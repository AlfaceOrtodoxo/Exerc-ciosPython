#006. Mostrar o dobro, o triplo e a raiz quadrada.

n_d06 = int(input('Digite um número: '))
dn_d06 = n_d06 * 2
tn_d06 = n_d06 * 3
rn_d06 = n_d06 ** (1 / 2)
print('O dobro de {} é {}.'.format(n_d06, dn_d06))
print('O triplo de {} é {}.'.format(n_d06, tn_d06))
print('A raíz quadrada de {} é {:.2f}.'.format(n_d06, rn_d06))