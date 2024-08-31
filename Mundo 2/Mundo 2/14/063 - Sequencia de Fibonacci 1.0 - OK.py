# Crie um programa que leia um número n e demonstre n números de sua sequência de Fibonacci.

n = int(input('Digite o número de termos da sequência a serem mostrados: '))

num1 = 0
num2 = 1
proxnum = num2
count = 1

while count <= n:
    print(proxnum, end=' ')
    count += 1
    num1, num2 = num2, proxnum
    proxnum = num1 + num2





