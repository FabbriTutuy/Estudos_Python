from rich import print
from rich.panel import Panel

class Gamer():

    def __init__(self,nome="<desconhecido>",nick="<desconhecido>"):

        self.nome = nome
        self.nick = nick

    lista_de_jogos = list()

    def Adicionar_Jogos(self,jogo):
        
        self.lista_de_jogos.append(jogo)
        self.lista_de_jogos.sort()

    def Ficha(self):
        
        txt = ""
        for j in self.lista_de_jogos:
            txt+=f"\n[bold blue]{j}[/]"

        personagem = Panel(f"nome: {self.nome} \nJogo Favorito: {txt}\n",title=f"nick:<{self.nick}>")
        print(personagem)


g1 = Gamer("Arthur Fabbri", "Tutuy_CDC")
g1.Adicionar_Jogos("GTA 5")
g1.Adicionar_Jogos("The Elder Scrolls: Skyrim")
g1.Adicionar_Jogos("Assasins Creed: Black Flag ")

g1.Ficha()
