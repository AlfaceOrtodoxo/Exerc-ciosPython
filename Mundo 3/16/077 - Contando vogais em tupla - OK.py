# Programa com tupla que tenha várias palavras (não usar acentos). Para cada palavra, deve mostrar quais são suas vogais.

palavras = ('aprender', 'programar', 'comer', 'dormir')

for palavra in palavras:
    print(f'\nNa palavra {palavra.title()} temos: ', end= '',)
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')


