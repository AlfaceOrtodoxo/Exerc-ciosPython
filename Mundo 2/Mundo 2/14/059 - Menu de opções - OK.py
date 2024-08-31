# Crie um programa que lê dois valores e mostre um menu:
# [1] para somar, [2] para multiplicar, [3] para escolher o maior, [4] para novos números e [5] para sair do programa.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

selec = 0

while selec != 5:
    print('\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair')
    selec = int(input('Digite a opção desejada: '))
    if selec == 1:
        print (f'A soma é {n1 + n2}.')
    if selec == 2:
        print (f'O produto é {n1 * n2}.')
    if selec == 3:
        print (f'O maior é {max(n1, n2)}.')
    if selec == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        