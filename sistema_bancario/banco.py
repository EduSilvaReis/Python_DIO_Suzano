import textwrap

def menu():
    """Mostra o menu de opções."""
    menu_string = """\n
    =============== MENU ===============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nu]\tNovo usuário
    [nc]\tNova conta
    [lc]\tListar contas
    [q]\tSair
    => """
    return input(textwrap.dedent(menu_string))


def depositar(saldo, valor, extrato, /):
    """
    Realiza a operação de depósito.
    Argumentos: saldo, valor, extrato (somente por posição).
    """
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza a operação de saque.
    Argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques (somente por nome).
    """
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    """
    Exibe o extrato da conta.
    Argumentos: saldo (por posição), extrato (por nome).
    """
    print("\n=============== EXTRATO ===============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\t\tR$ {saldo:.2f}")
    print("=======================================")


def criar_usuario(usuarios):
    """
    Cria um novo usuário.
    Verifica se o CPF já existe para evitar duplicidade.
    """
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com este CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    """Busca um usuário na lista por CPF."""
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    """
    Cria uma nova conta bancária.
    Vincula a conta a um usuário existente através do CPF.
    """
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario, "saldo": 0, "extrato": "", "numero_saques": 0}
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    """Lista todas as contas criadas."""
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def recuperar_conta_usuario(usuarios, contas):
    """
    Permite ao usuário selecionar uma conta.
    Busca o usuário pelo CPF e a conta pelo número.
    """
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\n@@@ Usuário não encontrado! @@@")
        return None, None

    numero_conta = int(input("Informe o número da conta: "))
    conta_filtrada = [c for c in contas if c["numero_conta"] == numero_conta and c["usuario"]["cpf"] == cpf]

    if not conta_filtrada:
        print("\n@@@ Conta não encontrada! @@@")
        return None, None

    return usuario, conta_filtrada[0]


def main():
    """Função principal que gerencia o fluxo do programa."""
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            usuario, conta = recuperar_conta_usuario(usuarios, contas)
            if conta:
                valor = float(input("Informe o valor do depósito: "))
                # A função 'depositar' ainda precisa ser refatorada para usar a 'conta'
                # Por enquanto, mantemos a chamada original
                conta['saldo'], conta['extrato'] = depositar(conta['saldo'], valor, conta['extrato'])

        elif opcao == "s":
            usuario, conta = recuperar_conta_usuario(usuarios, contas)
            if conta:
                valor = float(input("Informe o valor do saque: "))
                # A função 'sacar' ainda precisa ser refatorada para usar a 'conta'
                # Por enquanto, mantemos a chamada original
                conta['saldo'], conta['extrato'], conta['numero_saques'] = sacar(
                    saldo=conta['saldo'],
                    valor=valor,
                    extrato=conta['extrato'],
                    limite=500,
                    numero_saques=conta['numero_saques'],
                    limite_saques=LIMITE_SAQUES,
                )

        elif opcao == "e":
            usuario, conta = recuperar_conta_usuario(usuarios, contas)
            if conta:
                # A função 'exibir_extrato' ainda precisa ser refatorada para usar a 'conta'
                # Por enquanto, mantemos a chamada original
                exibir_extrato(conta['saldo'], extrato=conta['extrato'])

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Saindo do sistema. Obrigado por usar nosso banco!")
            break

        else:
            print("@@@ Operação inválida, por favor selecione a opção desejada. @@@")


if __name__ == "__main__":
    main()
