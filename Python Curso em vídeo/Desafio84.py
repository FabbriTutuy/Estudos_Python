
temp = list()
princ = list()
mai = men = 0

print("=-"*12 ,"Cadastro de Pessoas","=-"*12 )

while True:
    temp.append(str(input("Nome: ").capitalize()))
    temp.append(int(input("Peso: ")))

    if len(temp) == 0:
        mai = men = temp[1]

    else:

        if temp[1] > mai:
            mai = temp[1]
        
        elif temp[1] < men:
            men = temp[1]

    princ.append(temp[:])
    temp.clear()

    continuar = str(input("Deseja continuar: [S/N]")).upper()

    if continuar == "S":
        continue

    else:
        break

print("=-"*30)
print(f"Foram cadastrados {len(princ)} pessoas no cadastro")
print(f"O maior peso foi de {mai}" , end="")

for p in princ:
    if p[1] == mai:
        print(f"[{p[0]}]", end="")

print(f"\nE o menor peso foi de {men}")

for p in princ:
    if p[1] == men:
        print(f"[{p[0]}]" , end="")