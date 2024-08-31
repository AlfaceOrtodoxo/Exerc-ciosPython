#027. Programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro e o último nome separadamente, independente de quantos nomes tenha.


nome27 = input('Qual o teu nome? ')
primult = nome27.split()[::]
qtdnomes = int(len(primult))
numprim = primult[0]
numult = primult[(qtdnomes - 1)]
print("O seu primeiro nome é {} e o seu último nome é {}.".format(numprim, numult))

