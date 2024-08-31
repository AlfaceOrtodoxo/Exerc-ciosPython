#012. Programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preço = float(input('Quanto custa esse dereguejhonson aqui? '))
desconto = float(preço * 0.05)
preço_novo = float(preço - desconto)
print('Agora tá mais barato! Só R$ {:.2f}!'.format(preço_novo))
