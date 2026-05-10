# valores = list()

# for cont in range(0,5):
#     valores.append(int(input("Digite um valor: ")))

# print(f"Sua lista ficou {valores} assim!")

# for posicao ,valor in enumerate(valores):
#     print(f"Na posição {posicao} encontrei o calor {valor}!")

# print("Cheguei no final da lista")

a = [1,3,5,7,9]

#!!!!! ATENÇÃO !!!!!

b = a # Cria uma ligação
c = a[:] # Cria uma cópia
c[2] = 8

print(f"Lista A: {a}")
print(f"Lista B: {b}")
print(f"Lista C: {c}")