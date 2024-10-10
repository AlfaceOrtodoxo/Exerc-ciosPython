def aumentar(money: float, plus: float, format: bool) -> float:
    '''Essa função faz com que um valor seja aumentado em certa porcentagem.
    money:
        Float que recebe o valor que deseja manipular.
    plus:
        Float que recebe a porcentagem do aumento. Esse valor já é convertido automaticamente para porcentagem pela função.
    format:
        Bool que dá a opção de formatação para moeda ou não (USD ou BRL).
    '''
    calc = money * float(f'1.{plus}')
    if format == False:
        return calc
    else:
        currency = str(input('Selecione a moeda (USD ou BRL): ')).upper()
        return moeda(calc, currency)

def diminuir(money: float, minus: float, format: bool) -> float:
    '''Essa função faz com que um valor seja diminuido em certa porcentagem.
    money:
        Float que recebe o valor que deseja manipular.
    minus:
        Float que recebe a porcentagem do decréscimo. Esse valor já é convertido automaticamente para porcentagem pela função.
    format:
        Bool que dá a opção de formatação para moeda ou não (USD ou BRL).
    '''
    calc = money * float(f'1.{minus}')
    if format == False:
        return calc
    else:
        currency = str(input('Selecione a moeda (USD ou BRL): ')).upper()
        return moeda(calc, currency)

def dobro(money: float, format: bool) -> float:
    '''Essa função devolve o dobro de um valor.
    money:
        Valor a ser dobrado.
    format:
        Bool que dá a opção de formatação para moeda ou não (USD ou BRL).
    '''
    calc = money * 2
    if format == False:
        return calc
    else:
        currency = str(input('Selecione a moeda (USD ou BRL): ')).upper()
        return moeda(calc, currency)

def metade(money: float, format: bool) -> float:
    '''Essa função devolve a metade de um valor.
    money:
        Valor a ser dividido pela metade.'''
    calc = money / 2
    if format == False:
        return calc
    else:
        currency = str(input('Selecione a moeda (USD ou BRL): ')).upper()
        return moeda(calc, currency)

def moeda(money: float, currency: str) -> str:
    '''Essa função serve para formatar um valor para moeda.
    money
        Recebe o valor que será formatado.
    currency: Recebe 'USD' ou 'BRL'.
    '''
    money = str(f'{money:,.2f}')
    if currency == 'USD':
        return f'$ {money}'
    elif currency == 'BRL':
        money_br = money.replace(',', 'x').replace('.', ',').replace('x', '.')
        return f'R$ {money_br}'

