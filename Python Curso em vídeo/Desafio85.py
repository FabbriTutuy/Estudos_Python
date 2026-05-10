
numeros = [[],[]]

for cont in range(0,7):
    n = int(input(f"Digite o {cont+1}° número: "))
    
    if n % 2 == 0 :
        numeros[0].append(n)

    else:
        numeros[1].append(n)
        

print(f"O valores pares digitados par foram: {numeros[0]}")
print(f"Os valores impares digitados foram: {numeros[1]}")
print("")
