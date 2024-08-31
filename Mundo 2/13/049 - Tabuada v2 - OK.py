# Programa que use o laço for para mostrar a tabuada de um número escolhido pelo usuário.

n = int(input('Escolha um número: '))
for c in range(0,10):
    print(f'{n} * {c} = {n*c}')
print('FIM')
