# Programa que mostre a tabuada de vários números, um de cada vez, conforme solicita o usuário. Só para quando for inserido número negativo.

n = 0

while True:
    n = int(input('Digite um valor (negativo para sair do programa): '))
    if n < 0:
        break
    print(f'{n * 0}')
    print(f'{n * 1}')
    print(f'{n * 2}')
    print(f'{n * 3}')
    print(f'{n * 4}')
    print(f'{n * 5}')
    print(f'{n * 6}')
    print(f'{n * 7}')
    print(f'{n * 8}')
    print(f'{n * 9}')
    print(f'{n * 10}')

