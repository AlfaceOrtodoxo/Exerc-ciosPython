#Programa que leia o ano de nascimento de 7 pessoas e diga quantas já atingiram a maioridade (21 anos) e quantas ainda não.

import datetime

s = 0
n = 0
thisyear = datetime.datetime.now().year

for c in range (0,7):
    ano = int(input(f'Em que ano você nasceu? {c + 1}/7: ')) 
    if thisyear - ano >= 21:
        s += 1
    else:
        n += 1
print(f'{s} já atingiram a maioridade e {n} ainda não atingiram.')


