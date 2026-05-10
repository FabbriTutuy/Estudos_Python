
def LeiaInt(msg):
    
    ok = False
    valor = 0

    while True:

        n = str(input(msg))

        if n.isnumeric():
            valor = int(n)
            ok = True

        else:
            print("\033[0;31mERRO! DIGITE UM NÚMERO VALÍDO \033[m")

        if ok:
            break

    return valor


n = LeiaInt("Digite um número: ")
print(f"Você Digitou o número {n}")
