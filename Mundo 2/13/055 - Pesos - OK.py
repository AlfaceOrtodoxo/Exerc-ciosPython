#Programa que leia o peso de 5 pessoas e diga qual foi o maior e qual foi o menor.

maior = 0
menor = 0 
for p in range(1, 6):
    peso = int(input(f'Digite o peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    if maior > peso:
        maior = peso
    if menor < peso:
        menor = peso
        

print(f'O maior peso é {maior} e o menor é {menor}.')