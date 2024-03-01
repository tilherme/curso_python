def criar_saudacao(saudacao):
    def saudar(name):
        return f'{saudacao}, {name}!'
    return saudar

s1 = criar_saudacao('Bom dia')

s2 = criar_saudacao('Boa tarde')

print(s1('Gui'))
print(s2('Gui'))
