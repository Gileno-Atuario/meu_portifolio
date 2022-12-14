while True:
    valor = input('Digite o seu CPF (formato: 00000000000): ').strip()
    elementos = []
    for elemento in valor:
        elementos.append(elemento)
    if len(set(elementos)) == 1:
        print('Inválido! Valor não pode conter todos números iguais.')
        continue
    if len(valor) != 11:
        print('Inválido! Valor não contém 11 digitos.')
        continue
    if not valor.isnumeric():
        print('Inválido! Valor deve conter somente números.')
        continue
    i = 10
    soma = 0
    digito_x_regressao = []
    validacao = []
    validacao_strig =[]
    for j, l in enumerate(valor, start=1):
        if j < 10:
            validacao_strig.append(l)
            digito = int(l)
            validacao.append(digito)
            multiplicacao = digito * i
            digito_x_regressao.append(multiplicacao)
            i -= 1
            soma += multiplicacao
    soma_x_dez = soma * 10
    resto_divisao_por_11 = soma_x_dez % 11
    if resto_divisao_por_11 < 10:
        validacao.append(resto_divisao_por_11)
        validacao_strig.append(str(resto_divisao_por_11))
    else:
        maior_q_dez = 0
        validacao.append(maior_q_dez)
        validacao_strig.append(str(maior_q_dez))
    m = 11
    soma_1 = 0
    for n, o in enumerate(valor, start=1):
        if n < 11:
            digito_1 = int(o)
            multiplicacao_1 = m * digito_1
            soma_1 += multiplicacao_1
            m -= 1
    soma_x_dez_v2 = soma_1 * 10
    resto_divisao_por_11_v2 = soma_x_dez_v2 % 11
    if resto_divisao_por_11_v2 < 10:
        validacao.append(resto_divisao_por_11_v2)
        validacao_strig.append(str(resto_divisao_por_11_v2))
    else:
        maior_q_dez_v2 = 0
        validacao.append(maior_q_dez_v2)
        validacao_strig.append(str(maior_q_dez_v2))
    cpf = f'{valor[:3]}.{valor[3:6]}.{valor[6:9]}-{valor[9:]}'
    if elementos == validacao_strig:
        print(f'O CPF {cpf} É VÁLIDO!')
    else:
        print(f'O CPF {cpf} É INVÁLIDO!')

    opcao = input('Digite [s]air ou Enter(ou qualquer digito) para continuar: ').strip()
    if opcao.lower() == 's':
        quit()




