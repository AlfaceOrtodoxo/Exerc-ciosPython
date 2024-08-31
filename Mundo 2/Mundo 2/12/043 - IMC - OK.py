#Programa que calcule o IMC de alguém e classifique com base nisso:
# Abaixo de 18.5: Abaixo do peso.
# Entre 18.5 e 25: Peso ideal.
# 25 até 30: Sobrepeso.
# 30 até 40: Obesidade.
# Acima de 40: Obesidade mórbida.

peso = float(input('Quanto você pesa em quilos? '))
altura = float(input('Quanto você tem de altura? '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Você está abaixo do peso (IMC {:.2f})'.format(imc))
elif 18.5 < imc <= 25:
    print('Você está no peso ideal. (IMC {:.2f})'.format(imc))
elif 25 < imc <= 30:
    print('Você está com sobrepeso. (IMC {:.2f})'.format(imc))
elif 30 < imc <= 40:
    print('Você está obeso. (IMC {:.2f})'.format(imc))
else:
    print('Você está morbidamente obeso. (IMC {:.2f})'.format(imc)) 