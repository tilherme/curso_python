# cond = 10 == 0
# value = 'ok' if cond else 'nao ok' 
# print(value)
digito = 8
# new_digito = digito if digito <= 9 else 0
new_digito = 0 if digito > 9 else digito

print(new_digito)