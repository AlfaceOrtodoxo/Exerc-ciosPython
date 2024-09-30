# Crie um programa que tenha uma função fatorial() que recebe o numero e uma variável opcional lógica que decide se demonstra
# na tela o processo de cálculo ou não.


def fatorial(num, bool = False):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    if bool == False:
        return f
    else:
        print(f)
    
f1 = fatorial(5, True)

print(f1)