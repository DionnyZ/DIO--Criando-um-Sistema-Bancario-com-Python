operacao = ''
saldo = 0.0
extrato = ""
saque_diario = 0

print('Seja bem vindo ao Banco do Dionny!')

while operacao != '4':
    print(f'''\
        {'-' * 30}
        Qual operação deseja realizar?
        1 - Depósito
        2 - Saque
        3 - Extrato
        4 - Sair
    ''')

    operacao = input('Digite o número da operação: ')

    if operacao == '1':
        deposito = float(input('Informe o valor do depósito: '))

        if deposito > 0:
            saldo += deposito

            print(f'Foi depositado: R${deposito:.2f}')
            extrato += f'\nDepósito: R${deposito:.2f}'

        else:
            print('Valor inválido.')

    elif operacao == '2':
        if saque_diario >= 3:
            print('O limite de saques diários foi atingido. O limite é de 3 saques por dia.')

        else:
            saque = float(input('Informe o valor do saque: '))
            if saque > 500:
                print('O valor solicitado para o saque está acima do limite permitido. O valor máximo do saque é de R$500,00')

            elif saque > saldo:
                print(f'O valor solicitado para o saque está acima do saldo. Seu saldo é de: R${saldo:.2f}')

            else:
                saldo -= saque
                print(f'Saque de R${saque:.2f} realizado com sucesso. Saldo atual: R${saldo:.2f}')
                extrato += f'\nSaque: R${saque:.2f}'
                saque_diario += 1

    elif operacao == '3':
        print(f'Extrato:{extrato}')
        print(f'Saldo atual: R${saldo:.2f}')

    elif operacao == '4':
        print('Obrigado por utilizar nosso serviço. Até mais!')

    else:
        print('Operação inválida, selecione outra opção.')