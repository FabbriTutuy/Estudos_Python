
#LISTA

numeros = []

# DIGITAR VARIOS VALORES NUMERICOS  USANDO O WHILE 
# E JOGAR EM UMA LISTA  

while True:
    numero = int(input("Qual número deseja adicionar na sua lista: "))

    if numero in numeros:
        print("Não vou adicionar esse número ja existe lá")

    else:
        numeros.append(numero)
        print(f"O número {numero} foi adicionado com sucesso...!")

    continuar = input("Deseja continuar adicionando número: [S/N]").upper()

    if continuar == "S":
        continue   

    else:
        break

#DEIXAR EM ORDEM CRESCENTE 

numeros.sort()

#EXIBIR
print("Sua lista de número ficou assim: ", end="")

for n in numeros:
    print(f"{n}...", end="")