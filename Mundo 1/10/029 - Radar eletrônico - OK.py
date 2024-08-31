#029 Escreva um programa que leia a velocidade de um carro, avise se for multado e dê o valor da multa (R$7,00 para cada KM/h acima do limite de 80 KM/h).


speed29 = float(input('Qual a velocidade do carro? '))
if speed29 > 80.0:
    print('Você foi multado, mané!')
    valormulta = (speed29 - 80.0) * 7
    print('Tá devendo R$ {:.2f} pro Estado, seu fanfarrão.'.format(valormulta))
print('-----FIM-----')