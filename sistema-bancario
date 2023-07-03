# Depositar - somente valores inteiros positivos. Todos os depósitos devem ser armazenamos em uma variável e exibidos na operação extrato.
# Saque - permitido até 3 saques com limite máx. R$500,00. Caso o usuário nao tenha saldo na conta, exibir mensagem. Todos os saques devem ser armazenados em uma variável e exibidos na op. de extrato
# Extrato - listar todos os depósitos e saques realizados. Exibir saldo atual ao final. Formato - R$ xxx.xx


print(""" 
>>>> SISTEMA BANCÁRIO <<<<
Digite a operação que deseja:

    [ D ] Depósito
    [ S ] Saque
    [ E ] Extrato
    [ Q ] Sair
    """)

saldo = num_saques = 0
LIMITE_SAQUES = 3
limite = 500
extrato = ""


while True:
    print('=-' * 30)

    operação = str(input('Qual operação deseja realizar? ')).upper()[0]
    if operação == 'D':
        valor = float(input('-> Valor a ser depositado: R$ '))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Operação concluida com sucesso!")
        else:
            print('ERRO! Depósito não pode ser um valor negativo')

    elif operação == "S":
        valor = float(input('-> Valor a ser sacado: R$ '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = num_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("ERRO! Não há saldo suficiente para concluir essa transação.")
        elif excedeu_limite:
            print("ERRO! O valor do saque escede o limite.")
        elif excedeu_saques:
            print("ERRO! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            num_saques += 1
            print("Operação concluida com sucesso!")

    elif operação == 'E':
        print(f"\n{'EXTRATO':=^40}")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=" * 40)

    elif operação == 'Q':
        break

    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")
