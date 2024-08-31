#Programa onde o usuário possa digitar cinco valores numericos e cadastrá-los em uma lista já nas posições corretas sem usar o sort(). Mostrar em ordem crescente no final.

lista = []
n = 0

for c in range(0,5):
    if c == 0:
        lista.append(int(input('Digite um número: ')))
        print(f'O número {lista[0]} foi inserido na posição 0.')
    if c >= 1:
        n = int(input('Digite um número: '))
        if n > lista[len(lista) - 1]:
            lista.append(n)
            print(f'O número {n} foi adicionado à última posição da lista.')
        elif n < lista[0]:
            lista.insert(0, n)
            print(f'O número {n} foi adicionado à posição 0 da lista.')
        else:
            if lista[0] < n < lista[1]:
                lista.insert(1, n)
                print(f'O número {n} foi adicionado à posição 1 da lista.')
            elif lista[1] < n < lista[2]:
                lista.insert(2, n)
                print(f'O número {n} foi adicionado à posição 2 da lista.')
            elif lista[2] < n < lista[3]:
                lista.insert(3, n)
                print(f'O número {n} foi adicionado à posição 3 da lista.')    
print(lista)



