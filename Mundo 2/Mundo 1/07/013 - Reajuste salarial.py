#013. Programa que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.


salario = float(input('Quanto tu ganha, fio? '))
aumento = float(salario * 0.15)
novo_salario = float(salario + aumento)
print('Voa bixão, vai ganhar R$ {:.2f}!'.format(novo_salario))
