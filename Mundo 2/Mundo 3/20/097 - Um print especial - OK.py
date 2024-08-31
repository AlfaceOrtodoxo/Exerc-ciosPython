# Crie uma função 'escreva()' que receba um texto como parâmetro e o coloque entre linhas que se adaptam ao comprimento do texto.

def escreva(txt):
    tam = len(txt)
    print('-' * tam + '--')
    print(f'{txt:^{tam + 2}}')
    print('-' * tam + '--')

escreva('Tambaqui frito')
