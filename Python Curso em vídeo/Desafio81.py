
lista = []

while True:

    n = int(input("Digite um número para colocar na lista: "))
    lista.append(n)

    continuar = input("Deseja continuar S/N : ").upper()

    if continuar == "S":
        continue

    elif continuar == "N":
        break

    else:
        print("Isso não é uma resposta válida tente novamente!!")
        break

print(f"Sua lista {lista}")

print(f"Foram digitados {len(lista)} números na lista")
lista.sort()
print(f"A lista em forma decrescente ficou assim {lista}")

if 5 in lista:
    print(f"O número 5 está na lista e se encontra na posição ", end = "")
    
    for posicao,numero in enumerate(lista):

        if numero == 5:
            print(f"{posicao+1}..." , end="")

else:
    print("O número 5 não está na lista")