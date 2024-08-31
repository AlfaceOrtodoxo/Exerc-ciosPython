frase = "Até amanhã, jaçanã"
#fatiamento
#primeiro número: primeiro caractere
#segundo número: último caractere - 1
#terceiro número: casas a pular
print(frase[6:12:2])


#análise
#função len: len de length (comprimento)
print(len(frase))

#count: conta os caracteres, especificos
print(frase.count('a'))

#find: encontra algo na frase
print(frase.find('Até'))

#in
print('Até' in frase)


#transformação
#replace: substitui termo especifico
#.upper(), .lower(), .capitalize(), .title()
#.strip() remove espaços inuteis

#divisão
#.split() divide o string em lista
#''.join() junta a lista em um string só