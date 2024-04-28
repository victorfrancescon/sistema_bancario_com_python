def menu():
    menu = '''\n
    ----------Menu----------
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [nc] Nova Conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair
    
    '''
    return input(menu)


def depositar(saldo,valor,extrato, / ):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito: R$ {valor:.2f}\n'
        print('\n Deposito realisado com sucesso!')
    else:
        print('Operacao falhou')

    return saldo, extrato

def sacar (*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('Operacao falhou')

    elif excedeu_limite:
        print('Operacao falhou')
    
    elif excedeu_saques:
        print('Operacao falhou')

    elif valor > 0:
        saldo -= valor
        extrato += f'saque: R$ {valor: .2f}\n'
        print('Saque realizado com sucesso')
    
    else:
        print('Operacao falhou')

    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
    print('\n------Extrato------')
    print('Nao form realizados movimentacoes' if not extrato else extrato) 
    print(f'\nSaques R$ {saldo: .2f}')
    print('---------------------')

def criar_usuario(usuarios):
    cpf = input('informe o CPF (somente numeros): ')
    usuario = filtrar_usuario (cpf, usuarios)

    if usuario:
        print('ja existe usuario com esse CPF')
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento(dd-mm-aaaa): ')
    endereco = input('Informe o endereco (lograduro, nro - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('Usuario criado com sucesso')

def filtrar_usuario (cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuario: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Conta criada com sucesso ')
        return{'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('Usuario nao encontrado')

def listar_contas(contas):
    for conta in contas:
        linha = f'''
            agencia: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
            '''
        print('='* 100)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao =='d':
            valor = float (input ('Informe o valor do deposito: '))

            saldo, extrato = depositar(saldo,valor, extrato)

        elif opcao =='s':
            valor = float(input('Informe o valor do saque: '))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
        elif opcao =='e':
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == 'nu':
            criar_usuario(usuarios)
        
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break

        else:
            print('Operacao invalida')

main()