#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule a prestação mensal sendo que ela não pode exceder 30% do salário, ou então o empréstimo será negado.

valor = float(input('Qual é o valor da casa? R$ '))
salário = float(input('Qual é o valor do seu salário? R$ '))
anos = int(input('Em quantos anos você pretende pagar a casa? '))
anos_em_meses = anos * 12
prestacao = valor / anos_em_meses
if prestacao > (salário * 0.3):
    print('Sua prestação (R$ {:.2f}) é mais de 30% do seu salário ({:.2f}), portanto o seu financiamento não pode ser aprovado.'.format(prestacao, salário))
else:
    print('Parabéns, seu financiamento foi aprovado. O pagamento será feito em {:.0f} prestações de R$ {:.2f}.'.format(anos_em_meses, prestacao))