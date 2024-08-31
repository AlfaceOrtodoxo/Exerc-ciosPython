nome = str(input('Qual é o teu nome? '))
if nome == 'Gustavo':
    print ('que nome feio')
print ('Bom dia, {}!'.format(nome))

n1 = float(input('Qual foi a tua primeira nota? '))
n2 = float(input('Qual foi a tua segunda nota? '))
m = (n1+n2)/2
if m >= 6.0:
    print('Aprovado.')
else:
    print('Reprovado.')
    