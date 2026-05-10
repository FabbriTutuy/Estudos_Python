
numero_um = int(input("Digite um numero de 0 - 9: "))
numero_dois = int(input("Digite um numero de 0 - 9: "))
numero_tres = int(input("Digite um numero de 0 - 9: "))
numero_quatro = int(input("Digite um numero de 0 - 9: "))

tupla = (numero_um , numero_dois , numero_tres , numero_quatro)

print(f"O número nove apareceu {tupla.count(9)} vezes")

if 3 in tupla:
    print(f"o 3 está na {tupla.index(3)+1}ª posição")
else:
    print("O número 3 não está na tupla")

print("Os numeros pares são: ", end="")
for numero in tupla:
    if numero % 2 == 0:
        print(numero,end=" ")