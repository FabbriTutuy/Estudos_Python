
# Sistema simples de cadastro de clientes 
# Onde toda vez que for cadastrar um cliente colocar:
# Nome , email e número
# Terminado pode cadastrar um novo , mostrar todos e sair
# caso der erro deve tentar novamente e não acabar o script

# Opções do Sistema e dicionário

opcoes = """[1] Cadastrar um cliente
[2] Mostrar todos os clientes 
[3] Sair"""
opcao = 0
relatorio = ["=-"*20]

class Cliente:
    def __init__(self, nome , email, telefone):
        self.nome = nome
        self.email = email 
        self.telefone = telefone  

clientes = []

while True:
    print(opcoes)
    opcao = int(input("Qual opção você quer? "))

    if opcao == 1:
        nome = input("Qual o nome dele: ")
        email = input("Qual o email: ")
        telefone = input("Qual o telefone: ")

        # Cria um novo cliente e adiciona na lista
        cliente = Cliente(nome, email, telefone)
        clientes.append(cliente)

        # Adiciona ao relatório com quebra de linha
        relatorio.append(f"Nome: {nome}\nEmail: {email}\nTelefone: {telefone}\n{'=-'*20}")

    elif opcao == 2:
        print("\n===== RELATÓRIO DE CLIENTES =====")
        for item in relatorio:
            print(item)

    elif opcao == 3:
        break
    else:
        print("ERRO! Tente novamente.")

print("Obrigado por usar o programa! :)")
