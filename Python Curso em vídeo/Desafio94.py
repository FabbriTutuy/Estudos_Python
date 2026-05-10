
cadastro = dict()
lista = list()
media = 0

while True:
    
    cadastro["Nome"] = str(input("Nome: ")).capitalize()

    while True:
        cadastro["Sexo"] = str(input("Sexo [M/F]: ")).upper()[0]

        if cadastro["Sexo"] in "MF":
            break
        print("ERRO TENTE NOVAMENTE")

    cadastro["Idade"] = int(input("Idade: "))
    lista.append(cadastro.copy())
    cadastro.clear()

    while True: 
        continuar = str(input("Deseja continuar [S/N]: ")).upper()[0]
        
        if continuar in "SN":
            break

        print("ERRO TENTE NOVAMENTE")

    if continuar == "N":
        break

# =-=-=-=-=-=-=-=-= TEXTOS =-=-=-=-=-=-=-==-=
print("-="*30)

print(f" - O gurpo tem {len(lista)} pessoas")        # --> MOSTRA QUANTAS PESSOAS FORAM CADASTRADAS NA LISTA


for pessoa in lista:
    media+=pessoa["Idade"]
media = media / len(lista)      # --> MOSTRA A MÉDIA DE IDADE
print(F" - A média de idade foi {media} anos")


print(" - As mulheres cadastradas foram: " , end="")
for pessoa in lista:
    if pessoa["Sexo"] == "F":             # --> MOSTRA QUANTAS MULHERES ESTÃO NA LISTA
        print(pessoa["Nome"], end="")


print(f"\n - Lista das pessoas que estão acima da média:")
for pessoa in lista :
    if pessoa["Idade"] > media:           # --> MOSTRA QUANTAS PESSOAS ESTÃO ABAIXO DA MÉDIA
        print(f"nome = {pessoa["Nome"]}; sexo = {pessoa["Sexo"]}; idade = {pessoa["Idade"]}")

print("Volte sempre!!")
print("<< ENCERADO >>")