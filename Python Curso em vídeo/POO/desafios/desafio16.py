from rich import print

class Funcionario():
    
    def __init__(self,nome,setor,cargo,empresa="Curso em Video"):
        
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = empresa

    def Apresentar(self):

        return f"Olá, sou [bold blue]{self.nome}[/] e sou {self.cargo} no setor de {self.setor} da empresa {self.empresa}"


c1 = Funcionario("Pedro","TI" , "PROGRAMADOR JAVA")
print(c1.Apresentar())