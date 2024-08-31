# Programa que calcule o preço de um produto baseado na condição de pagamento.
# A vista dinheiro ou cheque: 10% de desconto.
# A vista no cartão: 5% de desconto.
# Em até 2x no cartão: Preço normal.
# Acima de 3x no cartão: 20% de juros.


preço = float(input('Qual é o preço do produto? R$ '))
parcelamento = int(input('O pagamento vai ser à vista? [S/N] ').lower)
if parcelamento == 's':
    parcelas = int(input('Em quantas parcelas você deseja pagar? '))
    if parcelas > 3:
        print('O produto vai custar R$ {:.2f}.'.format(preço * 1,2))
    else:
        print('O produto vai custar R$ {:.2f}.'.format(preço))
elif parcelamento == 'n':
    dinheirooucartão = str(input('O pagamento à vista vai ser no dinheiro, cheque ou cartão? ').lower)
    if dinheirooucartão == 'dinheiro' or 'cheque':
        print('O produto vai custar R$ {:.2f}.'.format(preço / 1.1))
    elif dinheirooucartão == 'cartão':
        print('O produto vai custar R$ {:.2f}.'.format(preço / 1.05))
        