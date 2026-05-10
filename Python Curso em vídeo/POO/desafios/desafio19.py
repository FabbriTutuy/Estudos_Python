from rich import print
from time import sleep

class Livro():
    
    def __init__(self,livro,paginas):
        
        self.livro = livro
        self.paginas = paginas

        print(f"Você acabou de ler o [bold blue]livro :'{livro}'[/] que tem [bold green]{paginas} paginas[/]")


    def passar_paginas(self,quantidade):
        
        paginas_total = self.paginas
        paginas_lidas = 0

        for n in range(1,quantidade+1):

            if paginas_total == paginas_lidas:
                break 

            else:

                sleep(0.3)
                paginas_lidas+=1
                print(f'Pág -> {n} ', end='')

        if paginas_total == paginas_lidas:
            print(f"\n[bold green]Você chegou ao fim do livro[/]")

        else:
            print(f"\n[bold yellow]Você avançou {quantidade} páginas e parou na página {quantidade+1}[/]")


l1 = Livro("O Homen que descobriou a lua",18)

l1.passar_paginas(10)