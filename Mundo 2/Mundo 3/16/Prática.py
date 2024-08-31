lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche) 
print(lanche[-1:-5:-1])

#TUPLAS SÃO IMUTÁVEIS

for c in lanche:    #maneira 1
    print (c)

for c2 in range(0, len(lanche)):     #maneira 2
    print (lanche[c2])

for pos, c3 in enumerate(lanche):  #maneira 3, mostra a posição
    print (f'{c3} na posição {pos}')

print(sorted(lanche)) #transforma em lista organizada em ordem alfabética

#tuplas podem ser somadas, e a ordem altera o resultado
#tuplas aceitam tipos diferentes de dados
#del() deleta uma variável ou tupla inteira
