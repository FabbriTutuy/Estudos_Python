from time import sleep

pessoas_cadastradas = [
    {"Nome":"Anna Paula Silva" , "Idade":21},
    {"Nome":"Rony Marcos Barbosa" , "Idade":18},
    {"Nome":"Pietro Martins Souza" , "Idade":67},
    {"Nome":"Ana Carolina Ferreira" , "Idade":41},
    {"Nome":"Miguel Ramos Souza" , "Idade":27},
    {"Nome":"Gabriela Gomes de Almeida" , "Idade":23}
]

temporaria = dict()

def menu():
    
    print("-"*38)
    print(F"{"MENU PRINCIPAL":^38}")
    print("-"*38)

    #FUNÇÕES

    print("1 - Ver pessoas cadatradas ")
    print("2 - Cadastrar uma nova pessoa")
    print("3 - Sair do sistema ")
    print("-"*38)


def cadastros():
    
    print("-"*38)
    print(f"{"PESSOAS CADASTRADAS":^38}")
    print("-"*38)

    for cadastros in pessoas_cadastradas:

        print(f"{cadastros["Nome"]:<28}  {cadastros["Idade"]:>2} anos")

    print("-"*38)


def novo_cadastro():

    while True:

        try :

            nome = str(input("Nome: ")).capitalize()

            while True:

                try:

                    idade = int(input("Idade: "))

                except:

                    print("\033[0;31mNÃO É UM NÚMERO INTEIRO VÁLIDO\033[m")

                else:

                    break

        except:

            print("\033[0;31mNÃO É UM NOME VÁLIDO!!\033[m")

        else:

            temporaria["Nome"] = nome
            temporaria["Idade"] = idade
            print(f"{nome} Cadastrado com sucesso idade = {idade}")
            pessoas_cadastradas.append(temporaria[:])
            temporaria.clear()
            break


# PROGRAMA PRINCIPAL

while True:

    menu()
    sleep(1.2)

    try:

        opcao = int(input("Qual função deseja acessar: "))


    except (ValueError, TypeError) as erro:

        print("\033[0;31mTENTE NOVAMENTE ISSO NÃO É UMA OPCÃO!!\033[m")

    else:

        sleep(1)

        try: 

            if opcao == 1:

                print("")
                cadastros()
                print("")

            elif opcao == 2:

                novo_cadastro()

            elif opcao == 3:

                break

            else:

                print("\033[0;31mESSA OPCÃO NÃO EXISTE!!\033[m")
                continue

        except:

            print()

print("")
print("OBRIGADO POR USAR O SISTEMA")

    


