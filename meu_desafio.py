def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor digitado não é válido.")
        
    return saldo, extrato

def sacar(valor, saldo, limite, numero_saques, LIMITE_SAQUES, extrato):
    excede_saldo = valor > saldo

    excede_limite = valor > limite

    excede_saques = numero_saques >= LIMITE_SAQUES

    if excede_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excede_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excede_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def extrato(saldo,  /, extrato):
    print("----------------EXTRATO----------------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("---------------------------------------")

def filtra_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(nome, data_nascimento, cpf, endereco, usuarios):
    usuario = filtra_usuarios(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def criar_conta_corrente(usuarios, AGENCIA, numero_conta):
    conta_tem_usuario = 0
    cpf=""

    while(cpf==""):
        cpf = int(input("Informe o CPF do usuário que é dono da conta: "))
        if(cpf==""):
            print("Nome do usuário da conta não pode ser vazio! Digite novamente.")
        usuario = filtra_usuarios(cpf, usuario)

    if(usuario):
        print("\nConta criada!")
        return {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("Este CPF não está registrado em nenhuma conta de usuário! Digite novamente.")

def main():
    menu = """
    ------------------MENU------------------
    (S) Sacar
    (D) Depositar
    (V) Visualizar extrato
    (U) Criar usuário
    (C) Criar conta corrente
    (X) Sair
    ----------------------------------------
    Digite a letra da operação desejada: 
    """
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    nome=""
    data_nascimento=""
    cpf=""
    endereco=""
    repetido = 0
    nome_usuario=""
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        operacao = input(menu)
        if operacao == "D":
            valor = float(input("Digite o valor a ser depositado: "))
            resultado = depositar(valor, saldo, extrato)
            print(f"Saldo = {resultado[0]:.2f} \n {resultado[1]}")

        elif operacao == "S":
            valor = float(input("Informe o valor a ser sacado: "))
            resultado = sacar(valor=valor, saldo=saldo, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES, extrato=extrato)
            print(f"Saldo = {resultado[0]:.2f} \n {resultado[1]}")

        elif operacao == "V":
            extrato(saldo, extrato=extrato)

        elif operacao == "U":
            while(nome==""):
                nome = str(input("Informe o nome do usuário: "))
                if(nome==""):
                    print("Nome não pode ser vazio! Digite novamente.")

            while(data_nascimento==""):
                data_nascimento = input("Informe a data de nascimento (dd/mm/yyyy): ")
                if(data_nascimento==""):
                    print("Data de nascimento não pode ser vazio! Digite novamente.")

            while(cpf==""):
                cpf = int(input("Informe o CPF: "))
                if(cpf==""):
                    print("CPF não pode ser vazio! Digite novamente.")

            while(endereco==""):   
                endereco = str(input("Informe o endereco (logradouro, numero - bairro - cidade/sigla_estado): "))
                if(endereco==""):
                    print("Endereco não pode ser vazio! Digite novamente.")

            criar_usuario(nome, data_nascimento, cpf, endereco, usuarios)

        elif operacao == "C":
            numero_conta = len(contas) + 1
            criar_conta_corrente(usuarios, AGENCIA, numero_conta)

        elif operacao == "X":
            print("Obrigado por usar o nosso banco! Tenha um bom dia.")
            break

        else:
            print("Operação inválida! Digite novamente.")