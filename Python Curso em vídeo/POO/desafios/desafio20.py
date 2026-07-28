from rich import print
from rich.panel import Panel

class Gamer():

    games = list()

    def __init__(self,nome,nick):
        self.nome = nome
        self.nick = nick


    def add_favorite_game(self,game):

        self.games.append(game)
        self.games.sort()



    def record(self):


        conteudo = f"Nome Real: [bold blue] {self.nome}[/]"
        conteudo += f"\nJogos Favoritos:"
        for jogo in self.games:
            conteudo += f"\n[blue]{jogo}[/]"
        
        record_complete = Panel(conteudo,title="Ficha Gamer",width=40)
        print(record_complete)


j1 = Gamer("Fabbri","Tutuy_CDC")
j1.add_favorite_game("Skyrim")
j1.add_favorite_game("Lethal Company")
j1.add_favorite_game("Counter Strike")
j1.record()
