
situação = dict()

situação["nome"] = str(input("Qual é o nome do aluno: ")).capitalize()
situação["nota"] = float(input("Qual é a nota do aluno: "))

print(f"Seu nome é {situação['nome']} ")
print(f"Sua média é {situação['nota']} ")
print(f"Situação é igual a ",end="")
if situação["nota"] >= 7:
    print("Aprovado")

else:
    print("REPROVADO")