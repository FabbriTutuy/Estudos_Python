
matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_par = list()
maior = list()
scol = 0

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

# SOMAR TODOS OS PARES DA MATRIZ

for l in matriz :
    for c in l:               # =-=-=-= DESCOBRIR QUAIS NÚMEROS SÃO PARES =-=-=-= #
        if c % 2 == 0:
            soma_par.append(c)

   # =-=-=-= SOMA DOS PARES =-=-=-= #         
        
for numero in soma_par:
    pass
        
print("=-"*12 , "CARACTERÍSTICAS DA MATRIZ","=-"*12)
print()    
print(f"A soma de todos os valores pares são: {sum(soma_par)}")

# SOMAR TODOS OS VALORES DA TERCEIRA COLUNA DA MATRIZ

for l in range(0,3):
    scol += matriz[l][2]
print(f"A soma da terceira coluna é: {scol}")

# E O MAIOR VALOR DA SEGUNDA COLUNA

for linha in matriz:
    maior.append(linha[1])

print(f"O maior número da segunda coluna é: {max(maior)}")