from time import sleep

jogador = dict()
jogadores = list()
gols = list()
total = 0

while True:
    jogador["nome"] = str(input("Qual o nome do jogador: ")).capitalize() # NOME DO JOGADOR E JOGA NO DIC

    jogador["partidas"] = int(input(f"Quantas partidas {jogador['nome']} jogou: "))  # QUANTOS JOGOS ELE JOGOU 

    for i in range(0,jogador["partidas"]):
        n = int(input(f"Quantos gols o {jogador['nome']} fez na {i+1}º partida: "))
        gols.append(n)          # --> FAZ UM LOOP NA QUANTIDADE DE JOGOS PARA SABER OS GOLS
        total+=n

    jogador["gols"] = gols[:]      # --> ADICIONA A QUANTOS GOLS O JOGADOR FEZ EM CADA PARTIDA     
    gols.clear()

    jogador["total_gols"] = total       # --> ADICIONA O TOTAL DE GOL FEITO PELO JOGADOR

    jogadores.append(jogador.copy())
    total = 0 
    jogador.clear()

    while True:

        continuar  = str(input("Deseja continuar [S/N]: ")).upper()[0]
        if continuar in "SN":
            break 

        else:
            print("COLOQUE SIM OU NÃO TENTE NOVAMENTE")
    
    if continuar == "N":
        break


print("=-"*30)
print(f'{"Nº":<4}{"NOME":<15}{"GOLS":<20}{"TOTAL":>6}')
print("-"*60)           #MOSTRA O TITULO DA TABELA

for i,joga in enumerate(jogadores):
    gols_str = ", ".join(map(str, joga['gols']))
    print(f"{i:<4}{joga['nome']:<15}{gols_str:<20}{joga['total_gols']:>6}")

while True:

    print("-"*30)
    mostrar_dados = int(input("Mostrar dados de qual jogador: "))

    if mostrar_dados in range(0,len(jogadores)):

        print(f"-- LEVANTAMENTO DO JOGADOR {jogadores[mostrar_dados]["nome"]}:")

        for i, gol in enumerate(jogadores[mostrar_dados]["gols"]):
            print(f"  No jogo {i+1} ele fez {gol} gols")

    elif mostrar_dados == 999:
        break

    else:
        print(f"ERRO  NÃO EXISTE JOGADOR CÓDIGO {mostrar_dados}! TENTE NOVAMENTE")

print("<< ENCERRADO >>")
