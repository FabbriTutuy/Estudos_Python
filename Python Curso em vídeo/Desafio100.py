from random import randint
from time import sleep

def pares():

    numeros = list()
    total = 0

    for n in range(0,5):

        n = randint(0,9)
        numeros.append(n)

        if n % 2 == 0:
            total+=n

    print(f"Sorteando os 5 valores da listas ",end="", flush=True)    
    for n in numeros:
        sleep(0.8)
        print(f"{n}.",end=" ",flush=True)
    print("PRONTO!")

    print(f"Somando os valores pares de {numeros}, temos {total}")

pares()
