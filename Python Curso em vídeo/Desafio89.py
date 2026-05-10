
ficha = list()

while True:
    nome = str(input("Nome: ")).capitalize()
    nota1 = float(input("Nota1: "))
    nota2 = float(input("Nota2: "))
    media = (nota1 + nota2)/2

    ficha.append([nome , [nota1 , nota2] , media])

    resp = str(input("Deseja continuar: S/N ").upper())

    if resp == "N":
        break

print("=-"*30)
print(f"{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}")
print("-"*26)

for i,a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{1:>8.1f}")

while True:
    print("-"*35)
    opc = int(input("Mostar nota de qual aluno: (999 interrompe): "))

    if opc == 999:
        print("FINALIZANDO...")
        break

    if opc <= len(ficha) - 1:
        print(f"Notas de {ficha[opc][0]} são {ficha[opc][1]}")