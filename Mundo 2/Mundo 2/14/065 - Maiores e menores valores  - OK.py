# Programa que vai ler vários números e só parará quando o usuário quiser. No final, mostre a média entre eles, o maior e o menor valor lidos. Também deve perguntar se o usuário quer continuar ou não.

qtd = num = sum = maior = menor = 0
continuar = ''
qtdmedia = 1

while continuar != 'N':
    num = int(input('Digite um número: '))
    qtd += 1
    qtdmedia += 1
    sum += num
    if qtd == 1:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    continuar = str(input('Você deseja acrescentar mais números? [S/N]: ')).upper()


print(f'A média dos {qtd} valores é {sum/qtdmedia}, o maior valor é {maior} e o menor é {menor}.')
