from rich import print
from rich.panel import Panel

class Produto():
    
    def __init__(self,nome,preco):

        self.nome = nome
        self.preco = preco

    
    def etiqueta(self):
        
        x = Panel(f"[bold white]{self.nome:.^35}\nR${self.preco:.^33}[/]",title="Produto")
        print(x)


p1 = Produto("Iphone 17 Pro max",12000.43)
p1.etiqueta()