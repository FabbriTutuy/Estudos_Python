from rich import print
from rich.panel import Panel

class Churrasco():

    # ATRIBUTOS DE CLASSE
    consumo_padrao:float = 0.400 # Cada pessoa consome em Média 400g de Carne
    preco_kg:float = 82.40 # Cada Kg de carne custa R$82,40

    def __init__(self,titulo,quantidade):
        
        # Atributos de Instância
        self.titulo = titulo
        self.quantidade = quantidade


    def __str__(self):

        return f"Esse é {self.titulo} com {self.quantidade} pessoas participando."
    

    def calcular_qtd_carne(self) -> float:

        return self.quantidade * Churrasco.consumo_padrao


    def calcular_custo_total(self) -> float:
        
        return self.calcular_qtd_carne() * self.__class__.preco_kg


    def calcular_preco_individual(self)-> float:
        
        return self.calcular_custo_total() / self.quantidade


    def analisar(self):

        conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.quantidade} convidados[/]"
        conteudo += f"\nCada participante comerá {Churrasco.consumo_padrao} Kg e cada Kg custa R${Churrasco.preco_kg:,.2f}"
        conteudo += f"\nRecomendo [blue]comprar {self.calcular_qtd_carne():.3f} Kg[/] de carne"
        conteudo += f"\nO custo total será de [green]R${self.calcular_custo_total():,.2f}[/]"
        conteudo += f"\nCada pessoa pagará [yellow]R${self.calcular_preco_individual():,.2f}[/] para participar."

        painel = Panel(conteudo, title=self.titulo) 
        print(painel)


c1 = Churrasco("Churrasco pra COPA",15)       
c1.analisar()