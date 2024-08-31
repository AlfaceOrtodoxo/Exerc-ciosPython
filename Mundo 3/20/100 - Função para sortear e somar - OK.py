# Faça um programa que tenha uma lista chamada números e duas funções chamadas 'sorteia()' e 'somaPar()'. A primeira função vai sortear 
# cinco números e colocá-los na lista, e a segunda função vai somar todos os valores pares da função anterior.
import random

lista = []


def main():
    somaPar(sorteia())


def sorteia():
    n = 0
    for i in range(0,5):
        n = random.randint(0, 100)
        lista.append(n)
    return lista
        

def somaPar(list):
    soma = 0
    for n in list:
        if n % 2 == 0:
            soma += n
    print(soma)
    

if __name__ == "__main__":
    main()


