
palavras = (
    "mercado",
    "lapis",
    "alho",
    "feijao",
    "banana",
    "luva"
)

for p in palavras:
    print(f"\nNa palavra {p} temos as vogai: ", end="")

    for letra in p:

        if letra.lower() in "aieou":
            print(letra, end=" ")