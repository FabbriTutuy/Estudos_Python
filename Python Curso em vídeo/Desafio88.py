from random import randint
from time import sleep

temporaria = list()
jogos = list()

print("=-"*15)
print("      JOGOS DA MEGA SENA")
print("=-"*15)
print()

numero_de_jogos = int(input("Quantos Jogos você deseja jogar: "))

print()
print(f"=-=-=-=-= SORTEIOS DOS {numero_de_jogos} NÚMEROS =-=-=-=-=")

for jogo in range(0,numero_de_jogos):
    for q in range(0,6):
        temporaria.append(randint(0,60))

    temporaria.sort()
    jogos.append(temporaria[:])
    temporaria.clear()

for contagem, jogo in enumerate(jogos):
    print(f"\nO {contagem+1}º jogo ficou assim: ",end="")
    
    for numero in jogo:
        print(numero,end=" ")
