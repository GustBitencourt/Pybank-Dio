import textwrap

def menu():
    menu = """Menu\n

        [d]\t - DEPOSITAR
        [s]\t - SACAR
        [e]\t - EXTRATO
        [nc]\t - Nova Conta
        [lc]\t - Listar Contas
        [nu]\t - Novo usuário
        [q]\t - SAIR

    """

    return input(textwrap.dedent(menu))

def saque(saldo, valor, extrato, limiteSaque, numeroSaque, LIMITE_SAQUES, /):
    
    if valor > saldo:
        print("Você não possui saldo suficiente.")
    elif valor > limiteSaque:
        print("Você ultrapassou seu limite disponível.")
    elif numeroSaque > LIMITE_SAQUES:
        print("Você ultrapassou seu limite de saques disponível.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque realizado no valor de {valor:.2f}\n"
        numeroSaque += 1
        print("Saque realizado!")
    else:
        print("Valor inválido")

    return saldo, extrato

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito realizado no valor de {valor:.2f}\n"
        print("Depósito concluído!")
    else:
        print("Não foi possível realizar a operação!")

    return saldo, extrato

def exibir_extrato(saldo, extrato, /):
    print("EXTRATO\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual de R$ {saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Informe CPF. Somente números: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário já existente")
        return
    
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento dd/mm/aaaa: ")
    endereco = input("Endereço. logradouro, num - bairro - cidade/sigla estado: ")

    usuario.append({"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})

    print("Usuário Criado com sucesso!!!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe seu cpf")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado. Operação encerrada")


def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
    
    print(textwrap.dedent(linha))


def main():
    saldo = 0
    limiteSaque = 500
    extrato = ""
    numeroSaque = 0
    usuarios = []
    contas = []

    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    while True:
        opcao = menu()

        if opcao == 'd':
            print("DEPÓSITO")
            valor = float(input("Valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)        

        elif opcao == 's':
            print("SAQUE")
            valor = float(input("Valor do depósito: "))

            saldo, extrato = saque(saldo, valor, extrato, limiteSaque, numeroSaque, LIMITE_SAQUES)        

        elif opcao == 'e':
            exibir_extrato(saldo, extrato)
        
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
            print("SAINDO")
            break
        else:
            print("Operação inválida, por favor seleciona novamente a operação desejada.")


main()