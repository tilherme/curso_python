perguntas = [
    {
        'pergunta' : 'quanto é 2 + 2?',
        'opções': ['3', '5','4'],
        'resposta': '4',

    },
    {
        'pergunta' : 'quanto é 2 + 3?',
        'opções': ['3', '5','4'],
        'resposta': '5',

    },
    {
        'pergunta' : 'quanto é 2 + 4?',
        'opções': ['4', '6','7'],
        'resposta': '6',

    },
]
qtd_acertos = 0
for pergunta in perguntas:
    print(pergunta['pergunta'])
    print('As Alternativas são: ')
    opcaos = pergunta['opções']
    for i, opcao in enumerate(opcaos):
        print(f'{i})',opcao)

    opcao = input('escolha uma das opções: ' )
    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcaos)
    if opcao.isdigit():
        escolha_int = int(opcao)
    if escolha_int >= 0 and escolha_int < qtd_opcoes:
        if opcaos[escolha_int] == pergunta['resposta']:
            acertou = True

    if acertou:
        qtd_acertos += 1

        print('🎉 acertou')
    else:
        print('😵 Errou')
print('Acertos', qtd_acertos)
    # i += 1
    