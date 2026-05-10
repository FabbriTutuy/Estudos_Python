from time import sleep
from random import randint 
from operator import itemgetter

geral = {
    "Jogador 1": randint(1,6),
    "Jogador 2": randint(1,6),
    "Jogador 3": randint(1,6),
    "Jogador 4": randint(1,6)
}
ranking = dict()

print("=-"*12,"Rodando","=-"*12)

for k,v in geral.items():
    sleep(1)
    print(f"O {k} tirou {v}")

ranking = sorted(geral.items() , key=itemgetter(1), reverse=True)

print("=== RANKING DOS JOGADORES ===")

for i,v in enumerate(ranking):
    sleep(1)
    print(f"{i+1}° Foi {v[0]} tirando {v[1]}")
    