#024. Programa que leia o nome de uma cidade e diga se começa ou não com SANTO.

nome24 = str(input('Qual o nome da tua cidade? '))
nome24.title()
nome24.split()
simoun24 = bool(nome24.find("Santo"))
simoun24 = not simoun24
print(simoun24)
