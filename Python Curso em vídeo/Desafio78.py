
numeros = []

#CRIAR UMA LISTA QUE VAI RECEBA 5 VALOR DO USUARIO
for posicao in range(0,5):
    numeros.append(int(input(f"Digite um número para colocar na posição {posicao}: ")))

print("=-"*25)
print(f"Sua lista ficou assim: {numeros}")      #Show list

#SABER O MENOR VALOR DIGITADO 
print(f"O maior Número é :{max(numeros)} Esse número se encontra nas posições: " , end="")

#create a 'for' loop to find out how many numbers were entered

for posicao,numero in enumerate(numeros):
    if numero == max(numeros):
        print(f"{posicao}..." , end="")

#KNOW A LARGER NUMBER
print(f"\nO Menor número é: {min(numeros)} Esse número se encronta nas posições: " , end="")

for posicao,numero in enumerate(numeros):
    if numero == min(numeros):
        print(f"{posicao}..." , end="")

print("\n","=-"*25)
