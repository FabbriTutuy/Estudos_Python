
lista = list()
lista_par = list()
lista_impar = list()

while True:
    lista.append(int(input("Digite um número para adicionar à lista: ")))
    continuar = input("Deseja continuar S/N: ").upper()

    if continuar == "S":
        continue

    elif continuar == "N":
        break

    else:
        print("ERROR TRY AGAIN !!!")

for numero in lista:
    if numero % 2 == 0 : 
        lista_par.append(numero)

    elif numero % 2 == 1:
        lista_impar.append(numero)

print(f"Sua lista de número ficou assim :{lista}")
print(f"Sua lista de número par ficou assim :{lista_par}")
print(f"Sua lista de número ímpar ficou assim :{lista_impar}")