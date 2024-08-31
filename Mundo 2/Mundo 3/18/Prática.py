teste = list()
teste.append('Natan')
teste.append(22)

galera = list()
galera.append(teste[:])

teste[0] = 'Jaum'
teste[1] = 16

galera.append(teste[:])

print (galera)