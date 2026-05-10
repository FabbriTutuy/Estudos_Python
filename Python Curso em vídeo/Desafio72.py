
numeros = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco',
    'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'quatorze', 
    'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)


while True:
    numero_do_usuario = int(input("Escolha um numero de 0 a 20: "))

    if 0 <= numero_do_usuario <= 20:
        print(f"O número que você escolheu por extenso fica: {numeros[numero_do_usuario]}")

        continua = input("Deseja continuar o programa: [s/n]").lower()

        if continua == "s":
            continue

        else:
            break

    print(f"Tente Novamente!. " , end="")

print("Obrigado por usar o programa")
