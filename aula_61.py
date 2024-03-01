while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador (/-+*): ')
    
    num_valido = None
    num_1_f = 0 
    num_2_f = 0

    try:
        num_1_f = float(num_1)
        num_2_f = float(num_2)
        num_valido = True

    except:
        num_valido = None
  
    if num_valido is None:
        print(' um dos numeros é invalido') 
        continue
    operador_permitido = '/-+*'

    if operador not in  operador_permitido:
        print('Operador invalido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    if operador == '+':
        print(f'{num_1} + {num_2} = {num_1_f + num_2_f}')
    elif operador == '-':
        print(f'{num_1} - {num_2} = {num_1_f - num_2_f}')
    
    elif operador == '/':
        print(f'{num_1} / {num_2} = {num_1_f / num_2_f}' )
    elif operador == '*':
        print(f'{num_1} * {num_2} = {num_1_f * num_2_f}')
    
    sair = input('Digite [s]im para sair : ').lower().startswith('s')
    print(sair)
    
    if sair is True:
        break
