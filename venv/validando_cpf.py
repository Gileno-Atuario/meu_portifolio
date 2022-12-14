import re
while True:
    entrada = input('Digite o seu CPF: ')
    cpf_usuario = re.sub(r'[^0-9]', '', entrada)
    elementos_cpf_usuario = []
    for elemento in cpf_usuario:
        elementos_cpf_usuario.append(elemento)
    if len(set(elementos_cpf_usuario)) == 1:
        print('Inválido! CPF não pode conter todos números iguais.')
        continue
    if len(cpf_usuario) != 11:
        print('Inválido! CPF não contém 11 digitos.')
        continue
    i = 10
    soma = 0
    digito_x_regressao = []
    validacao = []
    validacao_strig =[]
    for j, l in enumerate(cpf_usuario, start=1):
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
    for n, o in enumerate(cpf_usuario, start=1):
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
    cpf = f'{cpf_usuario[:3]}.{cpf_usuario[3:6]}.{cpf_usuario[6:9]}-{cpf_usuario[9:]}'
    if elementos_cpf_usuario == validacao_strig:
        print(f'O CPF {cpf} É VÁLIDO!')
    else:
        print(f'O CPF {cpf} É INVÁLIDO!')

    opcao = input('Digite [s]air ou Enter(ou qualquer digito) para continuar: ').strip()
    if opcao.lower() == 's':
        quit()




