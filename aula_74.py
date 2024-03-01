
lista_nomes = [ 'guilherme', 'Joaquim', 'Cristiane']
lista_nomes.append('Mateus')
lista_index = list(enumerate(lista_nomes))
# print(lista_index)
for index, nome in lista_index:
    # index, nome = i
    print(index, nome)