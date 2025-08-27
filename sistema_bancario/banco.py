def depositar(saldo, valor, extrato, /):
    """
    Função para realizar a operação de depósito.
    O '/' indica que os argumentos só podem ser passados por posição.
    """
    if valor > 0:
        saldo += valor  # Soma o valor ao saldo
        extrato += f"Depósito: R$ {valor:.2f}\n"  # Registra no extrato
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, extrato  # Retorna saldo e extrato atualizados


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Função para realizar a operação de saque.
    O '*' indica que todos os argumentos devem ser passados por nome.
    """
    excedeu_saldo = valor > saldo  # Verifica se o valor do saque é maior que o saldo
    excedeu_limite = valor > limite  # Verifica se o valor do saque excede o limite permitido
    excedeu_saques = numero_saques >= limite_saques  # Verifica se já atingiu o limite de saques

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques diários excedido.")

    elif valor > 0:
        saldo -= valor  # Subtrai o valor do saldo
        extrato += f"Saque: R$ {valor:.2f}\n"  # Registra no extrato
        numero_saques += 1  # Incrementa o número de saques
        print("\nSaque realizado com sucesso!")

    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques  # Retorna saldo, extrato e número de saques atualizados


def exibir_extrato(saldo, /, *, extrato):
    """
    Função para exibir o extrato bancário.
    O saldo deve ser passado por posição e o extrato por nome.
    """
    print("\n================ EXTRATO ================")
    # Se não houver movimentações, mostra mensagem; senão, mostra o extrato
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def main():
    """
    Função principal que gerencia o menu e a execução do programa.
    """
    MENU = """\n
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """

    saldo = 0  # Saldo inicial
    limite = 500  # Limite máximo por saque
    extrato = ""  # Extrato começa vazio
    numero_saques = 0  # Contador de saques realizados
    LIMITE_SAQUES = 3  # Limite de saques diários

    while True:
        opcao = input(MENU).lower()  # Mostra o menu e lê a opção do usuário

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            # Chama a função depositar passando argumentos por posição
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            # Chama a função sacar passando argumentos por nome
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            # Chama a função exibir_extrato passando saldo por posição e extrato por nome
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            print("Saindo do sistema. Obrigado por usar nosso banco!")
            break  # Sai do loop e encerra o programa

        else:
            print("Operação inválida, por favor selecione a opção desejada.")

# Executa a função principal quando o script é rodado diretamente
if __name__ == "__main__":
    main()