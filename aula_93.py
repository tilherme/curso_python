pessoa = {}
key = 'Nome'
key_last_name = 'Sobrenome'
pessoa[key] = 'Tii'
pessoa[key_last_name] = 'Mauricio'
del pessoa[key_last_name]
print(pessoa.get(key_last_name))
if pessoa.get(key_last_name) is None:
    print(pessoa)