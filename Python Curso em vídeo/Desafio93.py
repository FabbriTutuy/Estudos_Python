from time import sleep

jogador = dict()
gols = list()
total = 0

jogador["Nome"] = str(input("Qual o nome do jogador: ")).capitalize()
partidas = int(input(f"Quantas partidas {jogador["Nome"]} jogou: ")) 

for i in range(0,partidas):
    n = int(input(f"Quantos gols o {jogador['Nome']} fez na {i+1}º partida: "))
    gols.append(n)
    total+=n

jogador["Gols"] = gols
jogador["Total"] = total

print("-="*30)
sleep(1.2)
print(jogador)

print("-="*30)
sleep(1.2)
for k,v in jogador.items():
    print(f"O campo {k} tem o valor {v}")

print("-="*30)
sleep(1.2)
print(f"O jogador {jogador['Nome']} jogou {partidas}")
for i,jogo in enumerate(range(0,partidas)):
    print(f"    => Na partida {i+1}, fez {gols[i]} gols.")

print("=-=-=-= Obrigado por usar o Programa =-=-=-=")