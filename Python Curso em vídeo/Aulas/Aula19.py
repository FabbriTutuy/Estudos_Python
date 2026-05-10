# dados = {
#     "nome": "Gabriel",
#     "Idade" : 25
# }

# print(dados["nome"])
# print(dados)

# dados["sexo"] = "M"
# print(dados)

# del dados["Idade"]

# print(dados.values())      ##
# print(dados.keys())         ## DÁ PARA COMBINAR COM FOR
# print(dados.items())       ##

# filme = {
#     "titulo" : "Star Wars",
#     "ano": 1977,
#     "diretor" : "Geoge Lucas"
# }

# for k,v in filme.items():
#     print(f"O {k} é {v}")

# locadora = [
#     {
#         "titulo": "Star Wars",
#         "ano" : 1977,
#         "diretor": "George lucas"
#     },
#     {
#         "titulo": "Avengers",
#         "ano" : 2012,
#         "diretor": "Joss Whedon"
#     },
#     {
#         "titulo": "Matrix",
#         "ano" : 1999,
#         "diretor": "Wachowski"
#     }
# ]

# print(locadora[1]["ano"])

# pessoas = {
#     "nome":" Gustavo",
#     "idade":17,
#     "sexo": "M"
# }

# pessoas["nome"] = "Leaandro" # -> se eu fizer isso eu mudo o valor dentro da chave "nome"
# pessoas["peso"] = 95.5 # -> adiciona valor
# for k,v in pessoas.items():
#     print(f"{k} = {v}")

# brasil = list()
# estado1 = {
#     "uf":"Rio de Janeiro",
#     "sigla": "RJ"
# }
# estado2 = {
#     "uf":"São Paulo",
#     "sigla":"SP"
# }

# brasil.append(estado1)
# brasil.append(estado2)
# brasil+=[estado1,estado2]

# print(brasil)
# print(brasil[0]["sigla"])

estado = dict()
brasil = list()

for c in range(0,3):
    estado["uf"] = str(input("Unidade Federativa: "))
    estado["Sigla"] = str(input("Sigla: "))
    brasil.append(estado.copy())

print(brasil)

for e in brasil:
    for k,v in e.items():
        print(f"O campo {k} tal {v}")