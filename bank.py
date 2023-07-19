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
    elif opcao == 's':
        print("SAQUE")
    elif opcao == 'e':
        print("EXTRATO")
    elif opcao == 'q':
        print("SAINDO")
        break
    else:
        print("Operação inválida, por favor seleciona novamente a operação desejada.")