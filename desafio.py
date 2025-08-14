menu = """

[1] Adicionar saldo
[2] Realizar saque
[3] Consultar extrato
[0] Encerrar

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor para adicionar: "))

        if valor > 0 and valor:
            saldo += valor
            extrato += f"Depósito realizado: R$ {valor:.2f}\n"

        else:
            print("Erro! O valor informado não é válido.")

    elif opcao == "2":
        valor = float(input("Digite o valor para sacar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saque não autorizado! Saldo insuficiente.")

        elif excedeu_limite:
            print("Saque não autorizado! Valor acima do limite permitido.")

        elif excedeu_saques:
            print("Saque não autorizado! Limite diário de saques atingido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque realizado: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Erro! O valor informado não é válido.")

    elif opcao == "3":
        print("\n========== HISTÓRICO DE MOVIMENTAÇÕES ==========")
        print("Nenhuma transação registrada." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("===============================================")

    elif opcao == "0":
        print("Encerrando o sistema... Obrigado por utilizar nossos serviços!")
        break

    else:
        print("Opção inválida! Escolha uma das opções do menu.")
