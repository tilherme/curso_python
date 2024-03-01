# i = 1
# while i in range(1, 10):
#     print('Hello World!')
#     i += 1

# cond = True
# while cond:
#     print(input('Digite algo: '))
#     break
    # cond = False
# cont = 0

# while cont <= 100:
#     cont += 1 
    
#     if cont == 10:
#         continue
#     print(cont)

#     if cont == 29:
#         break

qtd_col = 5 
qtd_lin = 5

lin = 1

while lin <= qtd_lin:
    col = 1
    while col <= qtd_col:
        print(f'{lin=} {col=}')
        col += 1
    lin += 1
print('Fim do programa')
   