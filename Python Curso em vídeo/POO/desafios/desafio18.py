from rich import print
from rich.panel import Panel

class Churrasco():
    
    def __init__(self,nome = "Churrasco" , quantidade = 0):

        self.nome = nome
        self.quantidade = quantidade

    def Analisar(self):
        
        # CONSIDERE :
        # Consumo padrão: 400g p/pessoa
        # R$82,40/kg

        consumo_total = 0
        preco_total = (82.40*0.4)*self.quantidade
        preco_por_pessoa = preco_total/self.quantidade
        
        for pessoa in range(self.quantidade):
            consumo_total+=400

        consumo_kg = consumo_total/1000

        analise_completa = Panel(f"Analisando o [bold blue]{self.nome}[/] foram [bold green]{self.quantidade} pessoas[/]\nCada pessoa comerá 0.4Kg de carne e cada kilo custará R$82,40\nRecomendo comprar [bold yellow]{consumo_kg:.2f}Kg[/] de carne\nO custo total será de [bold purple]R${preco_total:.2f}[/]\nCada pessoa pagará [bold red]R${preco_por_pessoa}[/] para participar do [bold green]{self.nome}[/]",title=self.nome,style="bold white")
        print(analise_completa)


c1 = Churrasco("Churrasco de Cria",15)
c1.Analisar()
