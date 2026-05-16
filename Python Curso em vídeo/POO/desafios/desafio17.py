from rich import print
from rich.panel import Panel

class Produto():
    
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

    
    def etiqueta(self):
        
        conteudo = f"{self.nome.center(30, " ")}"
        conteudo += f"{'-'*30}"
        precof = f" R${self.preco:,.2f} "
        conteudo += f"{precof.center(30,'-')}"
        etiqueta_preco = Panel(conteudo,title="Produto",width=34)
        print(etiqueta_preco)

p1 = Produto("Iphone 17 Pro max",12_000.85)
p1.etiqueta()