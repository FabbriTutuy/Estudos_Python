
matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor para [{l} , {c}]: "))

print()
print("=-"*12,"FICOU ASSIM SUA MATRIZ","=-"*12)
print()

for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]}]", end="")
    print()