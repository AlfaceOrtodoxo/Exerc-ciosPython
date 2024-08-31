# Faça uma função que receba as dimensões de um terreno retangular e calcule sua área.

def area(h,l):
    s = h * l
    return s

def title(txt):
    print('-' * 40)
    print(f"{txt:^40}")
    print('-' * 40)


def main():
    title('CÁLCULO DE ÁREA')
    h = float(input('Qual é a altura do terreno, em m²?: '))
    l = float(input('Qual é a largura do terreno, em m²?: '))
    print(f'A área do terreno é {area(h,l):.2f} m².')
    title('FIM')

main()

