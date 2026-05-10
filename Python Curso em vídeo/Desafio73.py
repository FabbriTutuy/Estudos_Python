brasileirao = (
    "Botafogo",
    "Palmeiras",
    "Flamengo",
    "Atlético-MG",
    "Grêmio",
    "Fluminense",
    "Athletico-PR",
    "São Paulo",
    "Internacional",
    "Fortaleza",
    "Cuiabá",
    "Corinthians",
    "Cruzeiro",
    "Vasco da Gama",
    "Bahia",
    "Santos",
    "Goiás",
    "Coritiba",
    "América-MG",
    "Red Bull Bragantino"
)


print(f"Os 5 primeiros colocados são {brasileirao[0:6]}")
print(f"Os últimos 4 são {brasileirao[-4:]}")
print(f"Em ordem alfabética fica: {sorted(brasileirao)}")
print(f"O Flamengo ficou em {brasileirao.index("Flamengo")}º da posição")