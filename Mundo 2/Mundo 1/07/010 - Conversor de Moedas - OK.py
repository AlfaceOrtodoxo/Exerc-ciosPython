#010. Programa que leia quanto dinheiro uma pessoa tem e diga quantos dólares ela pode comprar (US$ 1.00 = R$ 3,27).

real_d010 = float(input('Quanta grana tu tem aí? '))
conversao_dolar = 3.27
dolar_d010 = float(real_d010 / conversao_dolar)
print('Você pode comprar US$ {:.2f}'.format(dolar_d010))
