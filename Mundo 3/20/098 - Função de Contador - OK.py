# Faça um programa que tenha uma função chamada 'contador()' que receba tres parametros: inicio, fim e passo e realize a contagem.
# faça com que conte: de 1 até 10 de 1 em 1, de 10 até 0 de 2 em 2 e uma contagem personalizada.
import time


def contador(inicio, fim, passo):
    if passo == 0:
        for i in range(inicio, fim, 1):
            print(f'{i} ',end='')
            #time.sleep(0.5)
    elif fim < inicio and passo > 0:
        for i in range(inicio, fim - 2, -(passo)):
            print(f'{i} ',end='')
            #time.sleep(0.5)
    else:
        for i in range(inicio, fim, passo):
            print(f'{i} ',end='')
            #time.sleep(0.5)


contador(1, 11, 1)
print()
contador(10, -1, -2)
print()
contador(int(input('Digite o primeiro número: ')), int(input('Digite o último número: ')) + 1, int(input('Digite o intervalo: ')))