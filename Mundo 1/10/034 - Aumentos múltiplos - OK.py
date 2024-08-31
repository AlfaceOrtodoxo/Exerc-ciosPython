#034 Escreva um programa que leia o salário de um funcionário e calcule seu aumento. Para salários maiores de 1250,00, 10%. Menores, 15%.


print('Você vai ganhar um aumento!')
sal033 = float(input('Quanto você ganha? '))
if sal033 <= 1250.00:
    valorme1250 = sal033 * 1.15
    print('Seu novo salário é {:.2f}.'.format(valorme1250))
else:
    valorma1250 = sal033 * 1.1
    print('Seu novo salário é {:.2f}.'.format(valorma1250))
print('-----FIM-----')