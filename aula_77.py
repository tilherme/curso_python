

frase = '      amanha é amanha, hoje é hoje       '
list_frase = frase.split(',')
list_frase_correta = []
for i, frase in enumerate(list_frase):
    list_frase_correta.append(list_frase[i].strip())

# print(list_frase_correta)
# print(list_frase)
unidas = ' === '.join(list_frase_correta)

print(unidas)