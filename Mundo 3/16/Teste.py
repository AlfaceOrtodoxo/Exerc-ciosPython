tup = ''
pares = ''
pos = ''
n9 = 0

for c in range(0,4):
    n = int(input('Número: '))
    if n % 2 == 0:
        pares += str(n) + ' '
    if n == 9:
        n9 += 1
    if n == 3:
        if c == 4:
            pos -= '  '
            pos += '.'
        else:
            pos += str(c) + ' '
    tup += str(n) + ' '

print (f'Os números foram: {tup}.')
if pares == '':
    print('Não há pares.')
else:
    print(f'Os pares são: {pares}')
print(f'O número 9 apareceu {n9} vezes.')
print(f'O número 3 aparece na(s) posição(ões) {pos}.')
