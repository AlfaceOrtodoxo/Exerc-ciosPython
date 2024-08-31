# 018. Faça um programa que leia um ângulo qualquer e mostre seu seno, cosseno e tangente.
# Pacote utilizado: Trigo


from trigo import sin, cos, tan
ang_d018 = float(input('Quanto mede o ângulo? '))
sin_d018 = sin(ang_d018)
cos_d018 = cos(ang_d018)
tan_d018 = tan(ang_d018)
print('O seno do ângulo é {}'.format(sin_d018))
print('O cosseno do ângulo é {}'.format(cos_d018))
print('A tangente do ângulo é {}'.format(tan_d018))