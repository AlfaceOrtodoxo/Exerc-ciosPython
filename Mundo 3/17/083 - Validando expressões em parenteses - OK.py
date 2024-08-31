#Programa que leia uma expressão matemática com parênteses qualquer e diga se os parênteses foram utilizados corretamente.


exp = str(input('Digite uma expressão: '))
abre = 0
fecha = 0

for c in exp:
    if c == '(':
        abre += 1
    if c == ')':
        fecha += 1

if abre == fecha and exp.find('(') < exp.find(')') and exp.find('(') + 1 != exp.find(')'):
    print('A expressão está correta.')
else:
    print('A expressão está incorreta.')

