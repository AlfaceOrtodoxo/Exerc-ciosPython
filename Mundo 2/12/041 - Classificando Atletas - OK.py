# Programa que leia a idade de um aluno de natação e diga a qual categoria ele pertence.
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUVENIL
# Até 20 anos: SÊNIOR
# Acima: MASTER

import datetime

data_atual = datetime.datetime.now()
ano_atual = data_atual.year
nascimento = int(input('Em que ano você nasceu? '))
idade = ano_atual - nascimento
if idade <= 9:
    print('Você está na categoria mirim.')
elif 9 < idade <= 14:
    print('Você está na categoria infantil.')
elif 14 < idade <= 19:
    print('Você está na categoria juvenil.')
elif 19 < idade <= 20:
    print('Você está na categoria sênior.')
else:
    print('Você está na categoria master.')