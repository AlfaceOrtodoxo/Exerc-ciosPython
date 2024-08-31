# Desenvolva um programa que leia nome e preço de vários produtos. Perguntar se o usuário quer continuar ou não.
# Deve mostrar: valor total da compra, quantos produtos custam mais de 1k, qual o nome do produto mais barato.

preço = total = umk = preçomenor = 0
nome = ''
continuar = ''
maisbarato = ''

while True:
    print ('------ Entre com os dados do produto ------')
    preço = float(input('Digite o preço do produto: '))
    nome = str(input('Digite o nome do produto: '))
    continuar = str(input('Tem mais produtos para registrar? [S/N]: ')).upper()
    maisbarato = nome
    preçomenor = preço
    total += preço
    if preço > 1000.00:
        umk += 1
    if preçomenor < preço:
        maisbarato = nome
    if continuar == 'N':
        break
print(f'O valor total foi R$ {total}, com {umk} produtos que custam mais de mil reais e o produto mais barato é {maisbarato}.')


