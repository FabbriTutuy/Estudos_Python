from rich import print
from rich import inspect

class Funcionario():
    
    empresa = "Curso em Vídeo"

    def __init__(self,nome,setor,cargo):
        
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def Apresentar(self) -> str:

        return f":handshake: Olá, sou [bold blue]{self.nome}[/] e sou {self.cargo} no setor de {self.setor} da empresa {Funcionario.empresa}."


c1 = Funcionario("Pedro","TI" , "PROGRAMADOR JAVA")
c2 = Funcionario("Maria","Administração","Financeiro")
print(c1.Apresentar())
print(c2.Apresentar())


#inspect(c1)    ----> SE UTILIZAR O INSPECT APARECERÁ ASSIM NO TERMINAL

#╭──────────── <class '__main__.Funcionario'> ─────────────╮
#│ ╭─────────────────────────────────────────────────────╮ │
#│ │ <__main__.Funcionario object at 0x00000272B6018C20> │ │
#│ ╰─────────────────────────────────────────────────────╯ │
#│                                                         │
#│   cargo = 'PROGRAMADOR JAVA'                            │
#│ empresa = 'Curso em Video'                              │
#│    nome = 'Pedro'                                       │
#│   setor = 'TI'                                          │
#╰─────────────────────────────────────────────────────────╯