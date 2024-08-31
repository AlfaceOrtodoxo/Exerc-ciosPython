# Crie um programa que leia as duas notas de um aluno e calcule sua média. Se < 5, REPROVADO. Se 5 < m < 6.9, RECUPERAÇÃO. Se >= 7, APROVADO.

n1 = float(input('Qual foi a sua primeira nota? '))
n2 = float(input('Qual foi a sua segunda nota? '))

media = (n1 + n2) / 2

if media < 5.0:
    print('O aluno está reprovado.')
elif 5.0 < media < 6.9:
    print('O aluno está de recuperação.')
else:
    print('O aluno foi aprovado.')