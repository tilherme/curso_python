def saudacao(msg,  nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return saudacao(funcao, *args)


print(executa('Bom dia', 'Gui'))
print(executa('Bom dia', 'joao'))
