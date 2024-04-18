
menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[0] Sair

'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

print('')
nome = input('Informe seu nome: \n')
print('\nBem vindo', nome.title())
print('Atualmete seu saldo é de: ', saldo)

while True:

    print('\ninforme a operação desejada')

    opcao = input(menu)

    if opcao == 'd':
        deposito = float(input('Informe quanto deseja depositar: '))
        if deposito <= 0:
            print('Operação inválida. Não é possivel depositar numero negativo')
        
        else:
            saldo += deposito
            extrato += 'Deposito: R$ ' + str(deposito) + '\n'
            print('\nDeposito realizado com sucesso!')
        
    elif opcao == 's':
        saque = float(input('Informe quanto deseja sacar: '))

        if saldo == 0 or saque > saldo:
            print('\nNão há saldo suficiente para saque!')

        elif saque > 500:
            print('\nO saque não pode ser superir a R$ 500.\n Por favor tente novamente.')

        elif saque <= 500:
            if LIMITE_SAQUES == numero_saques:
                print ('Limite de saques diarios atingido')

            else:
                print('\nOperação em andamento')
                print(' . ')
                print(' . ')
                print('Contando cedulas')
                print(' . ')
                print(' . ')
                print('Operação realizada com sucesso. Por favor retire o dinheiro.')

                numero_saques += 1
                saldo -= saque
                extrato += 'Saque: R$ ' + str(saque) + '\n'

    elif opcao == 'e':
        transacoes = f'''
    Suas ultimas transações foram:
    ################

{extrato}
    ################
        
    Seu saldo está em: R$ {saldo}

    ################
    '''

        print(transacoes)
    elif opcao == '0':
        break

    else:
        print('Operação invalida, por favor selecione novamente a operacao desejada.')