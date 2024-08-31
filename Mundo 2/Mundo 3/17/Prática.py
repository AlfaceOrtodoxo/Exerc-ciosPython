lanche = ['hamburguer', 'suco', 'pizza', 'pudim']

lanche.append('cookie') #adiciona elemento no fim da lista
lanche.insert(0, 'cachorro quente') #adiciona elemento em posição específica na lista
del lanche[3] #deleta por indice
lanche.pop(3) #deleta por indice, se não for indicado o ultimo elemento será eliminado
if 'pizza' in lanche:
    lanche.remove('pizza') #deleta pelo valor

valores = list(range(4,11)) #cria lista de elementos

# para ordenar os valores de uma lista

valores.sort()

# ordenar ao contrário

valores.sort(reverse=True)

numeros = []
numeros.append(5)
numeros.append(9)
numeros.append(4)

for c, v in enumerate(numeros):
    print(f'Na posição {c} eu encontrei o valor {v}!')
print('Cheguei ao final da lista.')

letras = []

for c in range(0,5):
    letras.append(str(input('Digite uma letra: ')))

print (letras)

# se uma lista for igualada a outra, as duas vão ser modificadas

a = [2, 3, 4, 5]
b = a # b e a estão ligadas
b = a[:]