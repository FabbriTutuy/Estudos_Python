
listagem = (
    "lápis" , 1.75,
    "borracha" , 2.90,
    "Caderno" , 20.50,
    "livro" , 15.60 ,
    "Estojo" , 12.50,
    "garrafa" , 19.25,
)

print("-"*38)
print(f"{"LISTAGEM DE PREÇOS":^38}")
print("-"*38)

for pos in range(0 , len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}",end="")

    else:
        print(f"R$ {listagem[pos]:>5.2f}")

print("-"*38)