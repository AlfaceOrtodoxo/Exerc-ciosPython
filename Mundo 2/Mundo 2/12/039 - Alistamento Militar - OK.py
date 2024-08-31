# Faça um programa que leia a idade de um jovem e diga se ele ainda vai se alistar, se está na hora de se alistar ou se já passou da hora de se alistar.
# O programa também deve dizer quanto tempo falta / passou do prazo.

import datetime
nascimento = int(input('Em que ano você nasceu? '))
data_atual = datetime.datetime.now()
ano_atual = int(data_atual.year)
idade = ano_atual - nascimento
if idade < 18:
    print(f'Você ainda não tem idade para se alistar. Faltam {18 - idade} anos.')
elif idade > 18:
    print(f'Você já passou {idade - 18} anos da idade de se alistar. Vá regularizar tua situação.')
else:
    print('Você está em idade de alistamento.')