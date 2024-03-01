import os
palavra = 'python'
letras_acertadas = ''
numero = 0
while True:
    letra_digitada = input('Digite uma letra: ')
    numero += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma lertra')
    if letra_digitada in palavra:
        letras_acertadas += letra_digitada
        palavra_formada = ''

        for letra_secreta in palavra:
            if letra_secreta in letras_acertadas:
                palavra_formada+= letra_secreta
            else:
                palavra_formada += '*'
        print('A palavra',palavra_formada)
        if palavra == palavra_formada:
            os.system('clear')
            print('VOCÊ ACERTOU PARABÉNS')
            print('A palavra é', palavra)
            print('VOCÊ VEZ EM', numero, 'TENTATIVAS')
            palavra = ''
            palavra_formada = ''