#Inserir alguma informação e dizer o que ela é
entrada = input('fala alguma coisa aí: ')
if entrada.isnumeric():
    print('teu negócio é um número men')
elif entrada.isalpha(): 
    print('teu negócio é uma letra men')
elif entrada.isalnum():
    print('teu negócio é uma letra e um número men')
else:
    print('sei la que que isso ai men')