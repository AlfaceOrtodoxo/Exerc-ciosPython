# Programa que vai ler vários números e só parará quando o usuário digitar 999. Quando tal, o programa mostrará quantos números foram digitados e a soma entre eles.

qtd = num = sum = 0

while num != 999:
    num = int(input('Digite um número (999 para parar): '))
    qtd += 1
    sum += num
print(f'A soma dos {qtd - 1} número(s) é {sum - 999}.')
