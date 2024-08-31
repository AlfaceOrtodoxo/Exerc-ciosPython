# Crie um programa que tenha uma tupla totalmente preenchida com contagem por extenso entre zero e 20.
# O programa deve ler um numero no teclado e mostrar o correspondente por extenso.

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input('Digite o número que quer ver por extenso, de 0 a 20: '))

while n < 0 or n > 20:
    n = int(input('Tente novamente. Digite o número que quer ver por extenso, de 0 a 20: '))

print(extenso[n].title())