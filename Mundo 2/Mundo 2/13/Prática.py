#for c in range(1,0):
#   comando dentro do laço
#comando fora do laço

for c in range(0,6):
    print('Oi')
print('Fim')

for d in range(0, 6, -1):
    print (d)
#o terceiro numero é o critério.

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i,f+1,p):
    print(c)
