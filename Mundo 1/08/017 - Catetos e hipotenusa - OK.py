# 017. Desenvolva um programa que calcule a hipotenusa de um triângulo por teorema de pitágoras, lendo o tamanho dos dois catetos.
# Pacote utilizado: BubbleMath

from BubbleMath import pythag
cat1_d017 = float(input('Quanto mede o cateto oposto? '))
cat2_d017 = float(input('Quanto mede o cateto adjascente? '))
hip_d017 = float(pythag(cat1_d017, cat2_d017))
print('A hipotenusa do triângulo retângulo é {:.2f}'.format(hip_d017))
