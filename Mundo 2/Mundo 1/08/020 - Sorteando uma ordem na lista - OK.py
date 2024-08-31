# 020. Um programa que sorteie uma ordem de nomes.
# Pacote utilizado: Random

import random
alunos_d020 = ['Zaza', 'Zeze', 'Zizi', 'Zozo']
primeiro_d020 = random.choice(alunos_d020)
alunos_d020.remove(primeiro_d020)
segundo_d020 = random.choice(alunos_d020)
alunos_d020.remove(segundo_d020)
terceiro_d020 = random.choice(alunos_d020)
alunos_d020.remove(terceiro_d020)
quarto_d020 = random.choice(alunos_d020)
print('A ordem de apresentação é: {}, {}, {} e {}.'.format(primeiro_d020, segundo_d020, terceiro_d020, quarto_d020))