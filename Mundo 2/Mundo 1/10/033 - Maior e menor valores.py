#033 Faça um programa que leia 3 números e diga qual o maior e qual o menor.


n1033 = int(input('Digite um número: '))
n2033 = int(input('Digite outro número: '))
n3033 = int(input('Digite mais um número: '))
if n1033 > n2033 > n3033 or n1033 > n3033 > n2033:
    print('O maior número é {}'.format(n1033))
if n2033 > n3033 > n1033 or n2033 > n1033 > n3033:
    print('O maior número é {}'.format(n2033))
if n3033 > n2033 > n1033 or n3033 > n1033 > n2033:
    print('O maior número é {}'.format(n3033))
print('-----FIM-----')
