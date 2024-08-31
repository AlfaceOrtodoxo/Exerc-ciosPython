#026. Programa que lê uma frase e diga quantas vezes aparece a letra A, qual a primeira posição que ela aparece, qual a última posição que ela aparece.

frase26 = str(input('Digite uma frase: '))
amaius = frase26.count("A")
aminus = frase26.count("a")
atotal = amaius + aminus
print("A letra A aparece {} vezes.".format(atotal))
frase26 = frase26.upper()
print(frase26.find("A"))
print(frase26.rfind("A"))
