import time



pessoas = {'nome': 'Natan', 'sexo': 'M', 'idade': 22}

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
time.sleep(0.5)
for k, v in pessoas.items():
    print(f'{k} = {v}')
    time.sleep(0.5)

#Dicionario não precisa de método append

#para fazer cópia de um dicionário, ao invés de fatiamento como para a lista ([:]), usamos o método interno copy()