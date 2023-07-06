import textwrap

def menu():
    menu = """\n
    ===================== MENU =====================
        [D] \tDepositar
        [S] \tSacar
        [E] \tExtrato
        [C] \tCriar Nova Conta
        [L] \tListar Contas
        [U] \tCriar Novo Usuário
        [Q] \tSair
    ...
    Digite sua opção => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \tR$ {valor:.2f}\n"
        print("\n:::Depósito realizado com sucesso:::")
    else:
        print("\n!!!ERRO: O valor informado é inválido!!!")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n!!!ERRO: Saldo insuficiente para concluir a operação!!!")
    elif excedeu_limite:
        print("\n!!!ERRO: O valor do saque excede o limite!!!")
    elif excedeu_saques:
        print("\n!!!ERRO: Número máximo de saques excedido!!!")
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque: \t\tR$ {valor:.2f}\n"
        print("\n::: Saque realizado com sucesso :::")
    else:
        print("\n!!!ERRO: O valor informado é inválido!!!")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n==================== EXTRATO ====================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: \t\tR$ {saldo:.2f}")
    print("====================================================")


def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n!!!ERRO: Já existe usuário com esse CPF!!!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome,
                     "data_nascimento": data_nascimento,
                     "cpf": cpf,
                     "endereco": endereco})

    print("::: Usuário criado com sucesso :::")


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n::: Conta Criada com Sucesso :::")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n!!!ERRO: Usuário não encontrado, fluxo de criação de conta encerrado!!!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
                Agência: \t{conta["agencia"]}
                C/C: \t\t{conta["numero_conta"]}
                Titular: \t{conta["usuario"]["nome"]}
                """
        print('=' * 50)
        print(textwrap.dedent(linha))



def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    numero_saques = 0
    limite = 500
    extrato = ""
    usuarios = []
    contas = []

    while True:
        opcao = menu().upper()[0]

        if opcao == "D":
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "S":
            valor = float(input('Informe o valor do saque: R$ '))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "E":
             exibir_extrato(saldo, extrato=extrato)

        elif opcao == "U":
             criar_usuario(usuarios)

        elif opcao == "C":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "L":
            listar_contas(contas)

        elif opcao == "Q":
            print("Programa finalizado. Até a próxima!")
            break

        else:
            print("Operação Inválida, por favor selecione novamente a operação desejada.")

main()
