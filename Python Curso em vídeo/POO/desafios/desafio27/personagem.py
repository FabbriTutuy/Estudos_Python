from abc import ABC,abstractmethod
import random
from rich import print
from rich.panel import Panel

class Personagem(ABC):

    def __init__(self,nome,vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []


    def atacar(self,alvo,forca = 50):

        if self.vida > 0 and alvo.vida > 0 :

            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            print(f"[green]{self.nome}[/]({self.vida}) atacou [red]{alvo.nome}[/]({alvo.vida}) com um [blue]{golpe}[/] de força [light blue]{forca}[/]")
            alvo.receber_dano(forca)

        else:
            print(f"O ataque {self.nome} -> {alvo.nome} não pode acontecer")


    def receber_dano(self,dano):

        fator = random.randint(0,dano)
        self.vida = self.vida - fator

        if self.vida < 0:
            self.vida = 0
        print(f"[blue]{self.nome}[/] recebeu [red]dano de {fator}[/]")

        
    @abstractmethod
    def curar(self):
        pass

    def status_personagem(self):
        pass



class Guerreiro(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco","Golpe de Machado","Pulo giratório"]

        
    def curar(self):
        fator = random.randint(0,100)
        self.vida += fator

        print(f"{self.nome} enrolou uma atadura nos ferimentos e [green]recuperou {fator} pontos[/] de vida")


    def status_personagem(self):

            conteudo = "[orange]Classe[/]: Guerreiro\n"
            conteudo += f"[bold blue]Nome[/]: {self.nome}\n"
            conteudo += f"[bold green]Vida[/]: {self.vida}\n"

            conteudo += f"{6*"=-"}= AÇÕES {6*"=-"}=\n"
            conteudo += "[purple]Ação 1[/]: Curar\n"
            conteudo += "[purple]Ação 2[/]: Atacar\n"

            conteudo += f"{6*"=-"}= ATAQUES {5*"=-"}=\n"
            for numero,glp in enumerate(self.golpes, start=1):
                conteudo += f"[red]Golpe[/] {numero}: {glp}\n"
            conteudo = conteudo.rstrip("\n")

            status = Panel(conteudo,title=f"Status do {self.nome}",width=37)
            print(status)


class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de Fogo","Nevasca","Faíscas"]


    def curar(self):
        fator = random.randint(0,100)
        self.vida += fator
        
        print(f"{self.nome} fez uma magia de cura e [green]recuperou {fator} pontos[/] de vida")


    def status_personagem(self):
        conteudo = "[orange]Classe[/]: Mago\n"
        conteudo += f"[bold blue]Nome[/]: {self.nome}\n"
        conteudo += f"[bold green]Vida[/]: {self.vida}\n"

        conteudo += f"{6*"=-"}= AÇÕES {6*"=-"}=\n"
        conteudo += "[purple]Ação 1[/]: Curar\n"
        conteudo += "[purple]Ação 2[/]: Atacar\n"
            
        conteudo += f"{6*"=-"}= ATAQUES {5*"=-"}=\n"
        for numero,glp in enumerate(self.golpes, start=1):
            conteudo += f"[red]Golpe[/] {numero}: {glp}\n"
        conteudo = conteudo.rstrip("\n")
            
        status = Panel(conteudo,title=f"Status do {self.nome}",width=37)
        print(status)



# FAZER SE O PERSONAGEM PODE ATACAR OU NÃO 
# E SE NÃO PODER O PORQUE 