
def linha(tam = 42):

    return "-"*42


def cabecalho(txt):

    print(linha())
    print(f"{txt:^42}")
    print(linha())


def menu(lista): 
    
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
        c+=1

    print(linha())

    opc = ReadInt("Sua opção: ")
    return opc

def ReadInt(msg):
    
    while True:

        try:                       # ---> TENTAR RODAR ESSE CODIGO
            num = int(input(msg))

        except Exception as erro:  # ---> EXCEÇÃO CASO DER ERRO

            print(f"\033[0;31mTente Novamente ERRO = {erro.__class__}\033[m")
            continue        # ---> JOGA DIRETO NO LAÇO WHILE NOVAMENTE

        else:                      # ---> CASO NÃO DER PROBLEMA/ DAR CERTO

            break

        finally:                   # ---> PARA FINALIZAR RODA EM QUALQUER DOS CASOS

            print("")

    return num


