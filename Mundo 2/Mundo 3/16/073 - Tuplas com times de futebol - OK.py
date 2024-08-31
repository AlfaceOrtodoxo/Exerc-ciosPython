# Crie tupla com os 20 primeiros colocados na tabela do brasileirão em ordem de colocação. Depois mostre:
# Apenas os primeiros 5 colocados, Os últimos quatro colocados, Lista em ordem alfabética e em qual posição está a Chapecoense.

colocaçao = 'botafogo', 'fortaleza', 'flamengo', 'palmeiras', 'são paulo', 'cruzeiro', 'bahia', 'atl pr', 'atl mg', 'juventude', 'vasco', 'bragantino', 'gremio', 'criciuma', 'internacional', 'vitoria', 'corinthians', 'fluminense', 'cuiaba', 'atl go'

g5 = colocaçao[0:4]
z4 = colocaçao[16:21]

print(f'O G5 é {g5};')
print(f'O Z4 é {z4};')
print(sorted(colocaçao))
print('A Chapecoense não está mais na primeira divisão.')