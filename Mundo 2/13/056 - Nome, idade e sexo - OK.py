# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# Deve mostrar: A média das idades, o nome do homem mais velho e quantas mulheres tem menos de 20 anos.

import datetime

esseano = datetime.datetime.now().year
idadesint = 0
mediaidade = 0
hmaisvelho = ''
idadehmaisvelho = 0
mulhermenos20 = 0

for c in range (1,5):
    print(f'------- {c}ª PESSOA -------')
    nomes = str(input('Digite o nome: ')).lower()
    idadesint =  (esseano - int(input('Em que ano nasceu: ')))
    sexo = str(input('Digite o sexo (M/F): ')).lower()
    mediaidade += idadesint
    if c == 1 and sexo == 'm ':
        hmaisvelho = nomes
        idadehmaisvelho = idadesint
    if sexo == 'm' and idadesint > idadehmaisvelho:
        hmaisvelho = nomes
        idadehmaisvelho = idadesint
    if sexo == 'f' and idadesint < 20:
        mulhermenos20 += 1


print(f'A média das idades é {mediaidade / 4}.')
print(f'O nome do homem mais velho é {hmaisvelho}, com {idadehmaisvelho} anos.')
if mulhermenos20 == 1:
    print(f'O grupo tem {mulhermenos20} mulher com menos de 20 anos.')
elif mulhermenos20 > 1:
    print(f'O grupo tem {mulhermenos20} mulheres com menos de 20 anos.')



