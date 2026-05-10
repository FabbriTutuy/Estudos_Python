
def fatorial(numero,show=0):
    
    """
    Docstring para fatorial
    
    :para numero: Qual número deseja fatoriar
    :param show: Se colocar True mostra passo a passo da fatoriação
    """

    if show != True: ## --> SE FOR DIFERENTE DE TRUE  -->  ""!=""

        fat = 1

        for num in range(numero,0,-1):
            fat*=num

        print(f"Os Resultados de {numero}! é {fat}")

    else:
        
        fat = 1

        for num in range(numero,0,-1):
            print(f"{num} x",end=" ")
            fat*=num

        print(f"= {fat}")


print(fatorial(4,True))
help(fatorial)
