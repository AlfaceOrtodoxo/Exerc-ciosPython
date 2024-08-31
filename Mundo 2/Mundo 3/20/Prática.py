def mensagem(msg):
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)

mensagem('TESTE')

#Empacotamento de parâmetros:

def contador(*num):
    for n in num:
        print(f'{n}, ', end= '')

contador(1, 2, 6, 8)

valores = [1, 2, 5, 8]

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

dobra(valores)
print(f'\n{valores}')