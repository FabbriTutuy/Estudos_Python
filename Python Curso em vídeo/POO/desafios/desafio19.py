from rich import print
from time import sleep

class Livro():

    def __init__(self,titulo,paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f":open_book: Você acabou de abrir o livro {self.titulo} que tem {self.total_paginas} páginas no total. Você agora está na página {self.pagina_atual}")


    def avancar_paginas(self, qtd = 1):

        cont = 0

        for pg in range(0,qtd,1):

            if not self.fim_do_livro():

                self.pagina_atual += 1
                print(f"Pág{self.pagina_atual} :arrow_forward: ", end="")
                sleep(0.4)
                cont += 1

        print(f"[blue]Você agora está na [yellow]página {self.pagina_atual}[/][blue]")

        if self.fim_do_livro():
            print(f":closed_book: [red]Você chegou ao final do livro {self.titulo}[/red]")


    def fim_do_livro(self) -> bool:

        return True if self.pagina_atual == self.total_paginas else False
    
        # =-=-=-=- Ou pode se fazer desse jeito -=-=-=-=
        #   if self.pagina_atual == self.total_paginas:
        #     return True
        #   else:
        #      return False


l1 = Livro("Senhor dos anéis",19)
l1.avancar_paginas(7)
l1.avancar_paginas(14)
