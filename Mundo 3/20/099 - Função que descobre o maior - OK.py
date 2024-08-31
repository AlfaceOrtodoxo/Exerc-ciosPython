#Faça uma função chamada 'maior()' que receba vários parâmetros com valores inteiros. O programa deve dizer qual é o maior.

def maior(*num):
   max = []
   for n in num:
      max.append(n)
   max.sort()
   print(max[len(max) - 1])

maior(0,2,9,8,5,4,)







