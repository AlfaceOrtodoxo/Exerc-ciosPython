# Agora o programa vai perguntar quantos termos da PA você quer ver a mais, e não vai parar até que o usuário diga 0.

n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termos = 1
count = 0
vzs = 0



while termos != 0:
    termos = int(input('\nQuantos termos você quer? '))
    vzs += 1
    count = 1
    if vzs == 1:
        print(n1, end=' ')
    while count < termos:
        count += 1
        n1 += r
        print (n1, end=' ')
    
    
 


