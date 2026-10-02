from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):

    sal_min = 1612
    inss = 7.5

    def __init__(self,nome = None, salario_bruto = 0, salario = 0):

        self.nome = nome
        self.salario_bruto = salario_bruto
        self.salario = salario

    @abstractmethod
    def calc_sal(self):
        
        pass


    def analisar_sal(self):
        
        base = self.salario/Funcionario.sal_min

        mensagem = f"O salário de [blue]{self.nome}[/] ({self.__class__.__name__}) é de [green]R${self.salario:.2f}[/] e corresponde a [yellow]{base:.2f} salários minímos[/]"
        painel = Panel(mensagem,title="Análise de Salário",width=50)
        print(painel)



class Horista(Funcionario):

    def __init__(self, nome , valor_hora = 7.37, qtd_horas=220):
        super().__init__(nome)  
        self.valor_hora = valor_hora
        self.horas_trabalhadas = qtd_horas
        self.salario_bruto = self.valor_hora * self.horas_trabalhadas
        

    def calc_sal(self):

        self.salario = self.salario_bruto - (self.salario_bruto * Funcionario.inss / 100)

class Mensalista(Funcionario):

    def __init__(self, nome , salario_bruto = Funcionario.sal_min):
        super().__init__(nome)
        self.salario_bruto = salario_bruto


    def calc_sal(self):

        self.salario = self.salario_bruto - (self.salario_bruto * Funcionario.inss / 100)
