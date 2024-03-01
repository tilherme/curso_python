nome = 'GuilhermeMateus'
i = 0
while i < len(nome):
    letra = nome[i]
    if letra == ' ':
        break
    print(letra)
    i += 1 
else:
    print('nao tem espaço')
print('tem espaço')