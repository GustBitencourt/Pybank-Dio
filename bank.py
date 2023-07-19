saldo = 0
limiteSaque = 500
extrato = ""
numeroSaque = 0
LIMITE_SAQUES = 3


menu = """

[d] - DEPOSITAR
[s] - SACAR
[e] - EXTRATO
[q] - SAIR

"""

while True:
    opcao = input(menu)

    if opcao == 'd':
        print("DEPÓSITO")
        valor = float(input("Valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito realizado no valor de {valor:.2f}\n"
        else:
            print("Não foi possível realizar a operação!")

    elif opcao == 's':
        print("SAQUE")
        valor = float(input("Valor do depósito: "))

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
        else:
            print("Valor inválido")

    elif opcao == 'e':
        print("EXTRATO\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual de R$ {saldo:.2f}")
    elif opcao == 'q':
        print("SAINDO")
        break
    else:
        print("Operação inválida, por favor seleciona novamente a operação desejada.")