# Desenvolva um programa que leia idade e sexo de várias pessoas. Perguntar se o usuário quer continuar ou não.
# Deve mostrar: quantas pessoas tem +18, quantos homens e quantas mulheres tem menos de 20 anos.

maioridade = homens = msub20 = 0
sexo = ''
idade = 0
continuar = '' 

while True:
    print('------ Digite os dados da pessoa ------')
    sexo = str(input('Homem ou mulher? [M/F]: ')).upper()
    idade = int(input('Digite a idade: '))
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        if idade < 20:
            msub20 += 1
    if continuar == 'N':
        break

print(f'Há {maioridade} maiores, {homens} homens e {msub20} mulheres abaixo de 20 anos.')    


