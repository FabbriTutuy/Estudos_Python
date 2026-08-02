from rich import print

class Caneta:

    def __init__(self,cor="azul"):

        escolha = ""
        match cor.lower().strip():

            case "azul":
                escolha = "[blue]"
            case "vermelho" | "vermelha":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case "roxo" | "roxa":
                escolha = "[purple]"
            case _:
                escolha = "[white]"

        self.cor = escolha
        self.tampada = True


    def escrever(self,msg):
        if self.tampada:
            print(f":prohibited: {self.cor}caneta[/] está tampada!")

        else:
            print(f"{self.cor}{msg}[/] ", end='')


    def quebrar_linha(self,qtd = 1):
        print("\n" * qtd, end='')


    def tampar(self):
        self.tampada = True


    def destampar(self):
        self.tampada = False


c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()

c1.escrever("Programar é dificil!")
c2.escrever("Porem não impossível!")
c2.quebrar_linha(2)
c3.escrever("Apenas continue!")

c1.tampar()
c2.tampar()
