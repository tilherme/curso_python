import re
import sys
entrada = input('CPF: ')
cpf = re.sub(
    r'[^0-9]',
    '',
    entrada
    ) 
entrada_rep = entrada == entrada[0] * len(entrada)
if entrada_rep:
    sys.exit()
nine = cpf[:9]
cont = 10
result = 0

for digito in nine:
    result += int(digito) *  cont
    cont -= 1
digito_1 = (result * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nine + str(digito_1)
cont_2 = 11
result_2 = 0

for digito in dez_digitos:
    result_2 += int(digito) * cont_2
    cont_2 -= 1
digito_2 = (result_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_calc = f'{nine}{digito_1}{digito_2}'

if cpf == cpf_gerado_calc:
    print(f'{cpf} é valido')
else:
    print('cpf invalido')