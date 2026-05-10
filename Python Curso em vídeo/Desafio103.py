def ficha(nome=0,gols=0):
    
    if nome == "":
        nome = "<DESCONHECIDO>"

    if gols == "":
        gols = 0

    print(f"O jogador {nome} fez {gols} gols na carreira")

print("-"*20)
jogador = str(input("Nome: ")).strip()
gol = str(input("Gols: ")).strip()

ficha(jogador,gol)