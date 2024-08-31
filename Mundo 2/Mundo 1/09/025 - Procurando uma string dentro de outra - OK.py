#025. Lê um nome e diz se tem SILVA no nome ou não.

nome25 = input('Qual o teu nome? ')
nome25.capitalize()
nome25.split()
simoun25 = bool(nome25.find("SILVA"))
simoun25 = not simoun25
print(simoun25)