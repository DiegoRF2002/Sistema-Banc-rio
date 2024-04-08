nome = input("\nBem vindo(a) ao DIO Bank! Antes de começar por favor, informe o nome do usuário: ")
print(f"Ótimo, seja bem vindo(a) {nome.title()}, vamos começar as operações!")

menu = '''
============== DIO Bank ==============
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

->'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Valor que deseja depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R${valor:.2f}\n'
            print(f"Operação concluida com sucesso {nome.title()}! depósito de R${valor:.2f} aprovado.")

        else:
            print(f"A operação falhou! {nome.title()}, o valor informado é insuficiente")

    elif opcao == "2":
        valor = float(input("Informe o valor qual deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print(f"Infelizmente {nome.title()}, o valor que deseja sacar é maior que o seu saldo atua. Operação interrompida.")
        
        elif excedeu_limite:
            print(f"Infelizmente {nome.title()}, o valor que deseja sacar é maior que o limite permitido. Operação interrompida.")

        elif excedeu_saques:
            print(f"Infelizmente {nome.title()}, o limite de saques diarios foi atingido.Tente novamente outro dia.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
            print(f"Operação concluida com sucesso {nome.title()}! Saque de R${valor:.2f} aprovado")

        else:
            print(f"A operação falhou! {nome.title()}, o valor informado é insuficiente")

    elif opcao == "3":
        print("\n=============== EXTRATO ===============")
        print(f"Usuário: {nome.title()}\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("=======================================")

    elif opcao == "0":
        break

    else:
        print(f"A operação falhou! {nome.title()}, selecione novamente a opção desejada.")
