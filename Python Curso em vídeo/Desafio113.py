
def ReadInt():
    
    while True:

        try:                       # ---> TENTAR RODAR ESSE CODIGO
            num = int(input("Digite Um número inteiro: "))

        except Exception as erro:  # ---> EXCEÇÃO CASO DER ERRO

            print(f"\033[0;31mTente Novamente ERRO = {erro.__class__}\033[m")
            continue        # ---> JOGA DIRETO NO LAÇO WHILE NOVAMENTE

        else:                      # ---> CASO NÃO DER PROBLEMA/ DAR CERTO

            break

        finally:                   # ---> PARA FINALIZAR RODA EM QUALQUER DOS CASOS

            print("")

    return num


def ReadFloat():
    
    while True:

        try:

            num = float(input("Digite um número Real: "))

        except Exception as erro:

            print(f"\033[0;31mTente novamente ERRO = {erro}\033[m")
            continue

        else:
        
            break

        finally:

            print("Valor registrado com sucesso")

    return num

inteiro = ReadInt()
real = ReadFloat()

print(f"O valor inteiro digitado foi {inteiro} e real foi {real:.2f}")