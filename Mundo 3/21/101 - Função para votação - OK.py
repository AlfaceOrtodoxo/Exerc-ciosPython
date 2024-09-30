# Crie uma função voto() que recebe o ano de nascimento como parâmetro e retorna NEGADO, OPCIONAL ou OBRIGATÓRIO.

import datetime as dt

def voto(ano):

    anoatual = int(dt.datetime.now().strftime('%Y'))
    
    if anoatual - ano >= 18:
        return 'OBRIGATÓRIO'
    elif 16 <= anoatual - ano < 18:
        return 'OPCIONAL'
    else:
        return 'NEGADO'
    

nascimento = int(input('Digite teu ano de nascimento: '))



decisão = voto(nascimento)

print(decisão)


