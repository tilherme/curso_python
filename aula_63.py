frase = 'Python é uma linguagem de programação' \
'Python foi criada por Guido Van Rossum'

i = 0 
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    qtd_letra_atual = frase.count(letra_atual)
    # print(letra_atual, qtd_letra)
    if letra_atual == ' ':
        i +=  1
        continue
    if qtd_apareceu_mais_vezes < qtd_letra_atual:
        qtd_apareceu_mais_vezes =  qtd_letra_atual
        letra_apareceu_mais_vezes = letra_atual

    
    i += 1
print('a letra', letra_apareceu_mais_vezes, 'qtd', qtd_letra_atual)
    
#     if qtd_apareceu_mais_vezes < qtd_mais_apareceu_atual:
#         qtd_apareceu_mais_vezes = qtd_mais_apareceu_atual
#         letra_mais_vezes = letra_atual
#     print(letra_apareceu_mais_vezes)
# print('quantidade',qtd_apareceu_mais_vezes,'letra' ,letra_apareceu_mais_vezes)