# Crie um programa que tenha uma tupla única com nomes e preços de produtos na sequência. No final, mostre uma listagem de preços organizados em forma tabular.

listagem = ('lapis', 1.75, 'borracha', 2.00, 'caderno', 15.90 )

for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end=' ')
    else:
        print(f'R$ {float(listagem[item]):>5.2f}')