import textwrap

def menu():
    """
    ================== MENU ==================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nu]\tNovo Usuário
    [nc]\tNova Conta
    [lc]\tListar Contas
    [q]\tSair

    => """
    return input(textwrap.dedent(menu))

def saque(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques


    if excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        return saldo, extrato

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
        return saldo, extrato  
    
    elif excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        return saldo, extrato


    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato

    else:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato

def deposito(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return saldo, extrato
    else:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato

def extrato_ver(saldo,/,*, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numero): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n@@@ Usuário já cadastrado. @@@")
        return
    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço: ")

    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    print("\n=== Usuário cadastrado com sucesso. ===")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso. ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado. @@@")

def filtrar_usuarios(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_filtrado = [usuario]
        else:
            usuario_filtrado = []
    if usuario_filtrado:
        return usuario_filtrado[0]
    else:
        return None

def listar_contas(contas):
    print("\n=== LISTA DE CONTAS ===")
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
    print("=" * 100)    
    print(textwrap.dedent(linha))
    
def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    contas = []
    usuarios = []
    

    while True:

        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == "e":
            extrato_ver(saldo, extrato=extrato)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
