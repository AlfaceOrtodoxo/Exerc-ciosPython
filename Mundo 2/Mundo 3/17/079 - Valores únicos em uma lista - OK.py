#Programa onde o usuário possa digitar varios valores numericos a serem cadastrados em lista. Caso já exista na lista ele não será cadastrado novamente.



n = 0
lista = []
cont = 'S'

while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('Número adicionado.')
    else:
        print('Já está na lista, não será adicionado.')
    cont = str(input('Deseja continuar? [S/N]: ')).upper()
    if cont in 'N':
        break
    

print(sorted(lista))