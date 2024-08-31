#Faça um programa que leia o sexo de uma pessoa mas só aceite valores M ou F. Deve pedir para redigitar se estiver errado até o correto ser digitado.

sexo = str(input('Você é M ou F?: ')).upper()

if sexo not in 'MF':

    while sexo not in 'MF':
        sexo = str(input('Vou perguntar de novo. Você é M ou F?: ')).upper()