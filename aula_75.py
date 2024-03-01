lista_compra = []
while True:

    option = input('Digite i[inserir], a[apagar] e l[listar] ')
    
    if len(option) > 1:
        print('Nao fooi possivel realizar comando ')
    if option == 'i':
        product = input('Digite seu produto: ')
        lista_compra.append(product)
    elif option == 'l':
        list_index = enumerate(lista_compra)
        for i, n in list_index:
            print(i, n )

    elif option == 'a':
        try:
            item = input('Qual item deseja apagar: ')
            m = int(item)
            del lista_compra[m]
        except:
            print('Produto não existe')