
def maior(*numeros):

    print("Analisando os valores passado...")

    for numero in numeros:
        print(numero,end=" ")

    print(f"Foram inforados {len(numeros)} valores ao todo")

    print(f"Sendo o {max(numeros)} maior numero dentre esses numeros")
    print("")


#INFORMAÇÕES / MAIN
maior(6,7,8,9,2,5)
maior(8,2,4,1)
maior(1,0,2)
maior(0)